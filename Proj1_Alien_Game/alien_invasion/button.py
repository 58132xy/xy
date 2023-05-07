import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        '''初始化按钮的属性'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和属性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # 按钮为亮绿色
        self.text_color = (255, 255, 255)  # 文本为白色
        self.font = pygame.font.SysFont(None, 48)  # None即为使用默认字体渲染，48为字号

        # 创建按钮的rect对象 ，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次,msg为要显示的文本
        self._preq_msg(msg)

    def _preq_msg(self, msg):
        '''将msg渲染为图像,并使文本在按钮居中'''
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)  # True为反锯齿功能
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充过的button，再绘制text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
