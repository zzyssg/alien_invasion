import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射的子弹进行管理"""

    def __init__(self, ai_settings, screen, ship):
        """飞船所属的位置创建一个子弹"""
        super().__init__()
        self.screen = screen

        """在（0,0）处创建一个子弹，然后移动到别处"""
        # 创建矩形,赋值给rect对象——提供左上角的x，y以及width、height
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """向上移动子弹"""
        # 更新代表子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹的rect
        self.rect.y = self.y

