import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按下"""
    if event.key == pygame.K_RIGHT:
        # 启动右移标志
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, bullets, screen, ship)
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


# 发射子弹
def fire_bullet(ai_settings, bullets, screen, ship):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        # 关闭右移标志
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # 重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # 让最近绘制的屏幕可见
    pygame.display.flip()


# 清除屏幕外的子弹
def update_bulltes(ai_settings, screen, ship, bullets, aliens):
    """更新子弹的位置，删除已经消失的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullets_aliens_collections(ai_settings, aliens, bullets, screen, ship)


def check_bullets_aliens_collections(ai_settings, aliens, bullets, screen, ship):
    """检查是否有子弹击中外星人，如果有则删除 此外星人 和 此子弹"""
    collections = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        """如果外星人被消灭完，则删除子弹，并新建一群外星人"""
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人 并计算一行能容纳多少外星人
    # 外外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    num_aliens_x = get_num_aliens_x(ai_settings, alien)
    rows = get_number_rows(ai_settings, alien.rect.height, ship.rect.height)

    # 创建第一行外星人
    for row in range(rows):
        for alien_num in range(num_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, alien_num, aliens, screen, row)


def get_num_aliens_x(ai_settings, alien):
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    num_aliens_x = int(available_space_x / (2 * alien_width))
    return num_aliens_x


def create_alien(ai_settings, alien_num, aliens, screen, row_num):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    aliens.add(alien)


def get_number_rows(ai_settings, alien_height, ship_height):
    """计算屏幕可容纳多少外星人"""
    available_space_y = ai_settings.screen_height - alien_height * 3 - ship_height
    num_rows = int(available_space_y / (2 * alien_height))
    return num_rows


def ship_hit(ai_settings, stats, screen, bullets, aliens, ship):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将剩余的飞船数量减1
        stats.ships_left -= 1
        # 清除外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人 + 将飞船放置中间
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()
        # 暂停0.5s
        sleep(0.5)
    else:
        stats.game_active = False


def update_aliens(ai_settings, stats, screen, bullets, aliens, ship):
    """更新所有外星人的位置"""
    # 检查是否有外星人到达边缘，更新整体外星人的位置
    check_fleet_edges(ai_settings, aliens)
    # 对编组调用的update()——将对每个分组调用update()方法
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, bullets, aliens, ship)
        print("Ship hit!")
    check_aliens_bottom(ai_settings, stats, screen, bullets, aliens, ship)


def change_fleet_direction(ai_settings, aliens):
    """将外星人下移 + 改变移动方向-左右互换"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """有外星人达到边缘时采用相应的措施"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_aliens_bottom(ai_settings, stats, screen, bullets, aliens, ship):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 同飞船被撞到
            ship_hit(ai_settings, stats, screen, bullets, aliens, ship)
            break
