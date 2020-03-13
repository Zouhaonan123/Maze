from numpy import *
import numpy as np
import random
import qlearning
import pygame
from button import Button
import screen_init
import time
import threading
from scoreboard import Scoreboard


process = 0


class draw(threading.Thread):
    def __init__(self, road, screen, x, image1, rect1, image2, rect2, grid):
        super().__init__()
        self.road = road
        self.screen = screen
        self.x = x
        self.image1 = image1
        self.rect1 = rect1
        self.image2 = image2
        self.rect2 = rect2
        self.grid = grid

    def run(self):
        count = 0
        scoreboard = Scoreboard(self.screen, count)

        for temp in self.road:

            screen_init.screen_init(self.screen, self.image2, self.rect2, self.x, self.grid)

            # 画出发点和终点
            pygame.draw.rect(self.screen, [0, 0, 255], [self.grid, self.grid, self.grid, self.grid], 0)
            pygame.draw.rect(self.screen, [255, 0, 0], [self.grid * (self.x.shape[1] - 2), self.grid * (self.x.shape[0] - 2), self.grid, self.grid], 0)

            self.rect1.center = (temp[1] * self.grid + (self.grid/2), temp[0] * self.grid + (self.grid/2))
            self.screen.blit(self.image1, self.rect1)
            scoreboard.show_count()
            pygame.display.flip()

            count += 1
            scoreboard.prep_count(count)

            print(temp[0], temp[1])
            time.sleep(0.05)

        for temp in self.road:
            pygame.draw.rect(self.screen, [255, 0, 0], [temp[1]*self.grid, temp[0]*self.grid, self.grid, self.grid], 0)
        self.rect1.center = (
        (self.x.shape[1] - 2) * self.grid + (self.grid / 2), (self.x.shape[0] - 2) * self.grid + (self.grid / 2))
        self.screen.blit(self.image1, self.rect1)

        pygame.display.flip()

        return


def qlearning_move(screen, x, image1, rect1, image2, rect2, grid):

    road = qlearning.qlearning_findroad(x)

    t1 = draw(road, screen, x, image1, rect1, image2, rect2, grid)
    t1.start()
    t1.join()