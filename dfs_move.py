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

        for i in range(self.road.size()):

            screen_init.screen_init(self.screen, self.image2, self.rect2, self.x, self.grid)

            # 画出发点和终点
            pygame.draw.rect(self.screen, [0, 0, 255], [self.startj*self.grid, self.starti*self.grid, self.grid, self.grid], 0)
            pygame.draw.rect(self.screen, [255, 0, 0], [self.grid * (self.x.shape[1] - 2), self.grid * (self.x.shape[0] - 2), self.grid, self.grid], 0)

            temp = self.road.pop()

            self.rect1.center = (temp[1] * self.grid + (self.grid/2), temp[0] * self.grid + (self.grid/2))
            self.screen.blit(self.image1, self.rect1)
            scoreboard.show_count()
            pygame.display.flip()

            count += 1
            scoreboard.prep_count(count)

            time.sleep(0.05)

        return


def dfs_move(screen, x, image1, rect1, image2, rect2, width, height, grid, starti, startj):

    road = dfs.findpath(starti, startj, width-2, height-2, x)
    t1 = draw(road, screen, x, image1, rect1, image2, rect2, grid, starti, startj)
    t1.start()
    t1.join()








