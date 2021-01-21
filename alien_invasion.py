import pygame
from pygame.sprite import Group

from setting import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

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

    # 创建开始按钮
    play_button = Button(ai_settings,screen,msg = "Play")

    # 初始化得分
    sb = ScoreBoard(ai_settings,screen,stats)
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb,play_button,ship,aliens, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()
            # 删除已经消失的子弹
            gf.update_bulltes(ai_settings, screen, stats,ship, bullets, aliens,sb)
            # 更新外星人的位置
            gf.update_aliens(ai_settings, stats, sb,screen,bullets, aliens, ship)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats,ship, aliens, bullets,play_button,sb)


run_game()
