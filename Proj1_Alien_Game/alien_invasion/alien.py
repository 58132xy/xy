import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    '''表示单个外星人的类'''

    def __init__(self,ai_game):
        '''初始化外星人并设置其起始位置'''
        super().__init__()
        self.screen = ai_game.screen

        self.settings = Settings()

        #加载外星人图像
        self.image = pygame.image.load('alien.bmp')
        self.image = pygame.transform.scale(self.image, (self.settings.alien_width, self.settings.alien_height))
        self.rect  = self.image.get_rect()

        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的精确水平位置
        self.x = float(self.rect.x)
        