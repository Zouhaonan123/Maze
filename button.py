import pygame.font


class Button():
    exist = False
    def __init__(self, screen, msg, x, y, button_color, text_color):
        self.screen = screen
        self.width, self.height = 120, 50
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 25)
        self.exist = True
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = [x, y]
        self.msg = msg
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.exist = True
        self.prep_msg(self.msg)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def change_color(self, color):
        self.button_color = color
        pygame.display.flip()

    def delete(self):
        self.exist = False
        self.prep_msg(' ')
        pygame.display.flip()


