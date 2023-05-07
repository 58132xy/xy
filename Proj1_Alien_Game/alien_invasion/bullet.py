import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''表示子弹的类'''

    def __init__(self, ai_game):
        '''在飞船当前位置创建一个子弹对象'''
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # 在（0，0）创建一个表示子弹的矩形并正确显示
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop  # 将子弹挪到飞船正上方

        # float存储更精确的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        '''子弹向上移动'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
