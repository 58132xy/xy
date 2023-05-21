import pygame
import sys

from time import sleep
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


class AlienInvasion:
    '''管理游戏资源和行为的类'''

    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Settings()

        # 指定屏幕大小
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # 实现全屏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # 创建存储游戏信息的实例
        self.stats = GameStats(self)
        # 创建飞船
        self.ship = Ship(self)
        # 存储子弹的列表
        self.bullets = pygame.sprite.Group()
        # 存储外星人的列表
        self.aliens = pygame.sprite.Group()
        # 创建外星人群
        self._creat_fleet()
        # 创建play按钮
        self.play_button = Button(self, "Play")
        # 创建记分牌
        self.sb = ScoreBoard(self)

    def _creat_alien(self, alien_number, row_number):
        '''创建一个外星人并将其放在当前行'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number  # 记得更新alien.x!不然只有一列外星人
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _creat_fleet(self):
        '''创建外星人群'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # 计算一行可容纳多少个外星人
        num_aliens_x = (self.settings.screen_width - 2 *
                        alien_width) // (2 * alien_width)
        # 计算可容纳多少行外星人
        num_aliens_y = (self.settings.screen_height - 3 *
                        alien_height - self.ship.rect.height) // (2 * alien_height)
        # 创建一排外星人，间隔为两个外星人宽度
        for alien_number in range(num_aliens_x):
            for row_number in range(num_aliens_y):
                self._creat_alien(alien_number, row_number)

    def _ship_hit(self):
        '''响应飞船被外星人撞到'''
        # 剩下命减一并更新剩余命数
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            # 清空剩下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人，并重置飞船位置
            self._creat_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            # 游戏结束后显示鼠标光标以便重新开始
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        '''更新所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()
        # 检测外星人和飞船间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 检测外星人是否到达底端
        self._check_aliens_bottom()

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
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                keydown_flag = event.type == pygame.KEYDOWN  # 按下为True，松开为Up
                self._check_key_events(event, keydown_flag)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''单击Play时开始游戏'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:  # 为了解决鼠标点击后再点击Play区域也会重置游戏bug
            # 重置游戏速度
            self.settings.initialize_dynamic_settings()
            # 重置统计信息，包括游戏活动标志置为True
            self.stats.reset_stats()
            # 重置得分，等级，剩余飞船数
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()
            # 创建一群新的外星人并让飞船居中
            self._creat_fleet()
            self.ship.center_ship()
            # 游戏开始后隐藏鼠标光标
            pygame.mouse.set_visible(False)

    def _check_key_events(self, event, keydown_flag):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = keydown_flag
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = keydown_flag
        if event.key == pygame.K_UP:
            self.ship.moving_up = keydown_flag
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = keydown_flag
        if event.key == pygame.K_q:
            sys.exit()
        if keydown_flag and event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # 删除消失的子弹，避免性能浪费
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # 检测是否击中外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)  # 两个true分别是删除碰撞的子弹和外星人,返回的是子弹-外星人列表的字典结构
        # 检测外星人是否全部消失，是则新生成一群
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        # 全部消灭后的处理
        if not self.aliens:
            self.bullets.empty()  # 删除现有子弹
            self._creat_fleet()  # 创建新的舰队
            self.settings.increase_speed()  # 提速增加难度
            self.stats.level += 1  # 增加等级
            self.sb.prep_level()

    def _check_aliens_bottom(self):
        '''检查是否有外星人到了屏幕底端'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞一样处理
                self._ship_hit()
                break

    def _update_screen(self):
        # 填充背景、绘制飞船并刷新屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # 显示得分
        self.sb.show_score()
        # 游戏非活动状态下创建Play按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    # 创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
