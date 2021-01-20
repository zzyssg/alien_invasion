class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""

        # 游戏刚开始时处于活动状态
        self.game_active = True

        # 屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹的设置 3像素宽
        self.bullet_speed_factor = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 屏幕中同时存在的子弹的最大数目
        self.bullets_allowed = 20

        # 外星人的移动速度
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # 向右移动direction = 1，左为-1
        self.fleet_direction = 1
