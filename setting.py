class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_limit = 0

        # 子弹的设置 3像素宽
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 屏幕中同时存在的子弹的最大数目
        self.bullets_allowed = 20

        # 外星人的移动速度
        self.fleet_drop_speed = 50

        # 以什么的加速度加快游戏速度
        self.speedup_scale = 1.2

        # 外星人点数的提高速度
        self.score_scale = 2

        # 动态变化
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        # 向右移动direction = 1，左为-1
        self.fleet_direction = 1

        # 每个外星人的分值
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置、外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points *self.score_scale)


