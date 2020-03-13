import pygame
import screen_init
import time
import threading
from scoreboard import Scoreboard
import bfs


class draw(threading.Thread):
    def __init__(self, road, screen, x, image1, rect1, image2, rect2, all, grid):
        super().__init__()
        self.road = road
        self.screen = screen
        self.x = x
        self.image1 = image1
        self.rect1 = rect1
        self.image2 = image2
        self.rect2 = rect2
        self.all = all
        self.grid = grid


    def run(self):
        count = 0
        scoreboard = Scoreboard(self.screen, count)

        for temp in self.all:

            pygame.draw.rect(self.screen, [255, 255, 0], [temp[1] * self.grid, temp[0] * self.grid, self.grid, self.grid], 0)
            pygame.display.flip()
            time.sleep(0.02)

        for i in range(self.road.size()):

            temp = self.road.pop()

            pygame.draw.rect(self.screen, [255, 0, 0], [temp[1] * self.grid, temp[0] * self.grid, self.grid, self.grid], 0)

            scoreboard.show_count()
            pygame.display.flip()

            count += 1
            scoreboard.prep_count(count)

            time.sleep(0.01)
        self.rect1.center = ((self.x.shape[1]-2) * self.grid + (self.grid / 2), (self.x.shape[0]-2) * self.grid + (self.grid / 2))
        self.screen.blit(self.image1, self.rect1)
        pygame.display.flip()

        return


def bfs_move(screen, x, image1, rect1, image2, rect2, width, height, grid, starti, startj):

    screen_init.screen_init(screen, image2, rect2, x, grid)

    # 画出发点和终点
    pygame.draw.rect(screen, [0, 0, 255], [startj*grid, starti*grid, grid, grid], 0)
    pygame.draw.rect(screen, [255, 0, 0], [grid * (x.shape[1] - 2), grid * (x.shape[0] - 2), grid, grid], 0)
    pygame.display.flip()

    road, all = bfs.bfs(starti, startj, width - 2, height - 2, x)
    t1 = draw(road, screen, x, image1, rect1, image2, rect2, all, grid)
    t1.start()
    t1.join()


