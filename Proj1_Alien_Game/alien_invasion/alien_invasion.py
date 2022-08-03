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

        # 指定屏幕大小
        # self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        # 实现全屏
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
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
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                moving_flag = event.type == pygame.KEYDOWN #按下为True，松开为Up
                self._check_key_events(event,moving_flag)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:  #摁下Q键退出
                    sys.exit()
                    
    def _check_key_events(self,event,moving_flag):
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