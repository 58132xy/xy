import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,ai_game):
        '''初始化外星人并设置其起始位置'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #加载外星人图像
        self.image = pygame.image.load('alien_invasion\Images\ship.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
        self.rect  = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的精确水平位置
        self.x = float(self.rect.x)

    def update(self):
        '''根据方向移动外星人'''
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x 

    def check_edges(self):
        '''如果有外星人在屏幕边缘,就返回true'''
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
            return True