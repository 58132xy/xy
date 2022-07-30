import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''表示飞船的类'''

    def __init__(self,ai_game):
        '''初始化外星人并设置其起始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并缩放尺寸
        self.image = (pygame.image.load("ship.bmp"))
        self.image = pygame.transform.scale(self.image, (50, 70))
        self.rect  = self.image.get_rect()

        #每个飞船都放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        #飞船的移动标志
        self.moving_right = False
        self.moving_left  = False
    
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right:
            self.rect.x += 1
            if self.rect.x > self.screen_rect.width:
                self.rect.x = self.screen_rect.width
        if self.moving_left:
            self.rect.x -= 1
            if self.rect.x == 0:
                self.rect.x = 0