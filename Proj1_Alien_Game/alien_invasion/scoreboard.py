import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    '''显示得分信息的类'''

    def __init__(self, ai_game):
        '''初始化显示得分涉及的属性'''
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息的字体
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # 准备初始化图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分渲染为图像'''
        score_str = 'Score:' + str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # 屏幕右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + 10

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)  # 四舍五入到最近十的整数倍
        high_score_str = 'High Score:' + str(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        # 将最高得分放在屏幕正中
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将等级渲染为图片'''
        level_str = 'Level:' + str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # 放于得分下方
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''显示还剩多少飞船'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.image = pygame.transform.scale(
                ship.image, (ship.settings.ship_width // 2, ship.settings.ship_height // 2))
            ship.rect.x = 10 + ship_number * ship.rect.width // 2
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        '''在屏幕上显示得分,最高得分，等级'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        '''检查是否发生了新的最高得分'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
