import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个存储子弹的编组
    bullets = Group()

    # 创建一组外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 创建一个用于存储 游戏统计信息 的实例
    stats = GameStats(ai_settings)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        if ai_settings.game_active:
            ship.update()
            bullets.update()
            # 删除已经消失的子弹
            gf.update_bulltes(ai_settings, screen, ship, bullets, aliens)
            # 更新外星人的位置
            gf.update_aliens(ai_settings, stats, screen,bullets, aliens, ship)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
