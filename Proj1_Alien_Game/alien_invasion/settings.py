class Settings:
    '''存储游戏《外星人入侵》中所有的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        #设置背景色为豆沙绿
        self.bg_color = (202,234,206)

        #飞船的速度
        self.ship_speed = 1.5

        #子弹的属性
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3 #只允许发射3颗子弹

        #外星飞船的属性
        self.alien_width = 100
        self.alien_height = 50
