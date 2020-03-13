
import numpy as np
from numpy import *
import random


def prim_maze(width=31, height=21):
    shape = (height, width)
    x = zeros(shape)
    k = 1
    z = ones(shape)

    for i in range(1, height-1, 2):
        for j in range(1, width-1, 2):
            x[i][j] = k
            k = k+1
            z[i][j] = 0
    loop = 0
    # 初始化墙列表
    wall = []
    wall.append(102)
    wall.append(201)
    while (x[1][1] != x[height-2][width-2]) | (x.max() != 1):
        wall_index = wall[random.randint(0, len(wall) - 1)]
        wall_i = wall_index // 100
        wall_j = wall_index % 100
        if wall_i % 2 == 0:
            if x[wall_i+1][wall_j] > x[wall_i-1][wall_j]:
                i = wall_i + 1
                j = wall_j
                x[wall_i + 1][wall_j] = x[wall_i - 1][wall_j]
                z[wall_i][wall_j] = 0
            elif x[wall_i+1][wall_j] < x[wall_i-1][wall_j]:
                i = wall_i - 1
                j = wall_j
                x[wall_i - 1][wall_j] = x[wall_i + 1][wall_j]
                z[wall_i][wall_j] = 0
        elif wall_j % 2 == 0:
            if x[wall_i][wall_j+1] > x[wall_i][wall_j-1]:
                i = wall_i
                j = wall_j+1
                x[wall_i][wall_j+1] = x[wall_i][wall_j-1]
                z[wall_i][wall_j] = 0
            elif x[wall_i][wall_j-1] > x[wall_i][wall_j+1]:
                i = wall_i
                j = wall_j-1
                x[wall_i][wall_j-1] = x[wall_i][wall_j+1]
                z[wall_i][wall_j] = 0

        if (i < height-2) & (j <width-2):
            wall.append((i+1)*100+j)
            wall.append(i*100+j+1)
        elif (i == height-2) & (j < width-2):
            wall.append(i*100+j+1)
        elif (i < height-2) & (j == width-2):
            wall.append((i + 1) * 100 + j)

        wall.remove(wall_index)
        loop = loop + 1
        # print(loop)
    return z
