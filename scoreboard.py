import pygame.font


class Scoreboard():
    def __init__(self, screen, count):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.count = count

        self.text_color = (200, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_count(count)

    def prep_count(self, count):
        count_str = str(count)
        self.count_image = self.font.render(count_str, True, self.text_color, (0, 255, 0))
        self.count_rect = self.count_image.get_rect()
        self.count_rect.right = self.screen_rect.right - 150
        self.count_rect.top = 30

    def show_count(self):
        self.screen.blit(self.count_image, self.count_rect)


