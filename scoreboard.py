import pygame.font

from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    """记录成绩"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示的分涉及到的类"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 定义分数的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 准备初始得分、最高得分、等级图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """将得分（文本）转化为图像"""
        rounded_score = round(self.stats.score,-1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)

        # 定义摆放位置
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image,self.screen_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        # 显示飞船剩余图像
        # 对编组调用draw，pygame会绘制每艘飞船
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """将最高得分转化为图像"""
        rounded_high_score = round(self.stats.high_score,-1)
        high_score_str = "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        # 定义摆放位置
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """将等级转化为图像"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str,True,self.text_color,self.ai_settings.bg_color)

        # 定义摆放位置
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示还剩下多少飞船"""
        self.ships = Group()
        for ship_num in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_num * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)




