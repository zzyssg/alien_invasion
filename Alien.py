import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """定义外星人的类"""

    def __init__(self,ai_settings,screen):
        """初始化外星人并设置其初始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """加载外星人图像，设置其rect属性"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """每个外星人初始都在屏幕左上角"""


        """存储外星人的准确位置"""

    def blitme(self):
        """指定位置绘制外星人"""
