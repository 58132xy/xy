import pygame
import sys

from settings import Settings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                moving_flag = True
                self._check_keydown_or_keyup_events(event,moving_flag)
            elif event.type == pygame.KEYUP:
                moving_flag = False
                self._check_keydown_or_keyup_events(event,moving_flag)
                    
    def _check_keydown_or_keyup_events(self,event,moving_flag):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = moving_flag
        if event.key == pygame.K_LEFT:
            self.ship.moving_left  = moving_flag
        if event.key == pygame.K_UP:
            self.ship.moving_up    = moving_flag
        if event.key == pygame.K_DOWN:
            self.ship.moving_down  = moving_flag

    def _update_screen(self):
        #填充背景、绘制飞船并刷新屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()

if __name__ == '__main__':
    #创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()