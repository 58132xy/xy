import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    '''表示飞船的类'''

    def __init__(self, ai_game):
        '''初始化飞船并设置其起始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并缩放尺寸
        self.image = pygame.image.load('alien_invasion\\Images\\ship.bmp')
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        # 每个飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船的移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 飞船的精细坐标
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # 记得更新rect对象！
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        '''让飞船在底部居中'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
