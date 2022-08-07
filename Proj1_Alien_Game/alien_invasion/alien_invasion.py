import pygame
import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()

        # 指定屏幕大小
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))

        # 实现全屏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self._update_ship()
            self._update_bullet()
            self._update_screen()

    def _check_events(self):
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keydown_flag = event.type == pygame.KEYDOWN #按下为True，松开为Up
                self._check_key_events(event,keydown_flag)
                    
    def _check_key_events(self,event,keydown_flag):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = keydown_flag
        if event.key == pygame.K_LEFT:
            self.ship.moving_left  = keydown_flag
        if event.key == pygame.K_UP:
            self.ship.moving_up    = keydown_flag
        if event.key == pygame.K_DOWN:
            self.ship.moving_down  = keydown_flag
        if event.key == pygame.K_q:
            sys.exit()
        if keydown_flag and event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom <= 0: #删除消失的子弹，避免性能浪费
                self.bullets.remove(bullet)
            bullet.draw_bullet()

    def _update_ship(self):
        self.ship.update()
        self.ship.blitme()

    def _update_screen(self):
        #填充背景、绘制飞船并刷新屏幕
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    #创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()