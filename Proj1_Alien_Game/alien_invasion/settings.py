class Settings:
    '''存储游戏《外星人入侵》中所有的类'''

    def __init__(self):
        '''初始化游戏的静态设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色为豆沙绿
        self.bg_color = (202, 234, 206)

        # 飞船属性
        self.ship_width = 50
        self.ship_height = 70
        self.ship_limit = 3

        # 子弹属性
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3  # 只允许发射3颗子弹

        # 外星飞船属性
        self.alien_width = 100
        self.alien_height = 50
        self.fleet_drop_speed = 50  # 外星人的速度

        # 加快游戏节奏的速度
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 0.5
        self.fleet_direction = 1  # 1表示向右移，-1表示向左移
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度设置及外星人分数'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
