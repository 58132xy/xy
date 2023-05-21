class GameStats:
    '''跟踪游戏的统计信息'''

    def __init__(self, ai_game):
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()

        # 游戏开始处于非活动状态
        self.game_active = False

        # 最高得分，不得重置
        self.high_score = 0

    def reset_stats(self):
        '''初始化统计信息'''
        self.ships_left = self.settings.ship_limit  # 重新3条命
        self.game_active = True
        self.score = 0
        self.level = 1
