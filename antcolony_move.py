import numpy as np
import antcolony
import pygame
import dfs
import screen_init
import time
import threading
from scoreboard import Scoreboard


class draw(threading.Thread):
    def __init__(self, road, screen, x, image1, rect1, image2, rect2, grid, starti, startj):
        super().__init__()
        self.road = road
        self.screen = screen
        self.x = x
        self.image1 = image1
        self.rect1 = rect1
        self.image2 = image2
        self.rect2 = rect2
        self.grid = grid
        self.starti = starti
        self.startj = startj

    def run(self):
        count = 0
        scoreboard = Scoreboard(self.screen, count)

        for temp in self.road:

            screen_init.screen_init(self.screen, self.image2, self.rect2, self.x, self.grid)

            # 画出发点和终点
            pygame.draw.rect(self.screen, [0, 0, 255], [self.starti*self.grid, self.startj*self.grid, self.grid, self.grid], 0)
            pygame.draw.rect(self.screen, [255, 0, 0], [self.grid * (self.x.shape[1] - 2), self.grid * (self.x.shape[0] - 2), self.grid, self.grid], 0)

            self.rect1.center = (temp[1] * self.grid + (self.grid/2), temp[0] * self.grid + (self.grid/2))
            self.screen.blit(self.image1, self.rect1)
            scoreboard.show_count()
            pygame.display.flip()

            count += 1
            scoreboard.prep_count(count)

            time.sleep(0.05)
        for temp in self.road:
            pygame.draw.rect(self.screen, [255, 0, 0], [temp[1]*self.grid, temp[0]*self.grid, self.grid, self.grid], 0)
        pygame.display.flip()

        return


def antcolony_move(screen, x, image1, rect1, image2, rect2, grid, starti, startj):
    screen_init.screen_init(screen, image2, rect2, x, grid)

    # 画出发点和终点
    pygame.draw.rect(screen, [0, 0, 255], [grid, grid, grid, grid], 0)
    pygame.draw.rect(screen, [255, 0, 0], [grid * (x.shape[1] - 2), grid * (x.shape[0] - 2), grid, grid], 0)

    map = antcolony.Map(x, x.shape[0], x.shape[1], starti, startj, x.shape[0]-2, x.shape[1]-2)
    road = antcolony.findpath(map)
    # print(road)
    t1 = draw(road, screen, x, image1, rect1, image2, rect2, grid, starti, startj)
    t1.start()
    t1.join()

