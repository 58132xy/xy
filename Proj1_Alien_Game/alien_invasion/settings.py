class Settings:
    '''存储游戏《外星人入侵》中所有的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色为豆沙绿
        self.bg_color = (202, 234, 206)

        # 飞船的速度
        self.ship_speed = 1.5
        self.ship_limit = 3

        # 子弹的属性
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3  # 只允许发射3颗子弹

        # 外星飞船的属性
        self.alien_width = 100
        self.alien_height = 50

        # 外星人的速度
        self.alien_speed = 0.5
        self.fleet_drop_speed = 50
        # self_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
