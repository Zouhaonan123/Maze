import numpy as np
import pygame


def screen_init(screen, image, rect, x, grid):
    screen.fill([0, 191, 255])  # 屏底色
    # 画墙体
    for i in range(0, x.shape[0]):
        for j in range(0, x.shape[1]):
            if x[i][j]:
                rect.center = (j*grid+(grid/2), i*grid+(grid/2))
                screen.blit(image, rect)