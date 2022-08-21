import pygame
import sys

from settings import Settings
from ship import Ship
from alien import Alien
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

        #创建飞船
        self.ship = Ship(self)
        #存储子弹的列表
        self.bullets = pygame.sprite.Group()
        #存储外星人的列表
        self.aliens  = pygame.sprite.Group()
        #创建外星人群
        self._creat_fleet()

    def _creat_alien(self,alien_number,row_number):
        '''创建一个外星人并将其放在当前行'''
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        alien.x = alien_width + 2*alien_width*alien_number #记得更新alien.x!不然只有一列外星人
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2*alien_height*row_number
        self.aliens.add(alien)

    def _creat_fleet(self):
        '''创建外星人群'''
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        #计算一行可容纳多少个外星人
        num_aliens_x = (self.settings.screen_width - 2*alien_width) // (2*alien_width)
        #计算可容纳多少行外星人
        num_aliens_y = (self.settings.screen_height - 3*alien_height - self.ship.rect.height) // (2*alien_height)
        #创建一排外星人，间隔为两个外星人宽度
        for alien_number in range(num_aliens_x):
            for row_number in range(num_aliens_y):
                self._creat_alien(alien_number,row_number)

    def _update_aliens(self):
        '''更新所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        '''有外星人到达屏幕边缘时更新方向及位置'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_aliens()
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
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0: #删除消失的子弹，避免性能浪费
                self.bullets.remove(bullet)

    def _update_screen(self):
        #填充背景、绘制飞船并刷新屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    #创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()