from numpy import *
import numpy as np
import random
import pygame
import button


global q, r


def find(row, col, r):
    for i in range(0, r.shape[0]):
        if (r[i][0] == row) and (r[i][1] == col):
            return i
    print("not found")


def qlearning_learning(x):

    alpha = 0.8
    belta = 0.8
    # 查找所有的路
    a = x == 0
    global q, r
    r = zeros((sum(a), 7))
    q = zeros((r.shape[0], r.shape[1] - 2))
    # k为路的数量
    k = 0
    for i in range(0, a.shape[0]-1):
        for j in range(0, a.shape[1]-1):
            if a[i][j]:
                r[k][0] = i
                r[k][1] = j
                k = k + 1
    r[:, 2:] = -100
    for i in range(0, k-1):
        row = int(r[i][0])
        col = int(r[i][1])

        if a[row-1][col]:
            r[i][2] = -1
        if a[row+1][col]:
            r[i][4] = -1
        if a[row][col-1]:
            r[i][3] = -1
        if a[row][col+1]:
            r[i][5] = -1

        if not a[row-1][col]:
            q[i][0] = -100
        if not a[row+1][col]:
            q[i][2] = -100
        if not a[row][col-1]:
            q[i][1] = -100
        if not a[row][col+1]:
            q[i][3] = -100

        if (row == x.shape[0]-1) and (col == x.shape[1]-2):
            r[i][2] = 100
        if (row == x.shape[0]-3) and (col == x.shape[1]-2):
            r[i][4] = 100
        if (row == x.shape[0]-2) and (col == x.shape[1]-1):
            r[i][3] = 100
        if (row == x.shape[0]-2) and (col == x.shape[1]-3):
            r[i][5] = 100

    r[:-1, -1] = -1
    r[-1, -1] = 100
    for loop in range(0, 10):
        # i = random.randint(0, k-1)
        i = 1
        times = 0
        while i != k-1:
            row = int(r[i][0])
            col = int(r[i][1])

            s = sum(r[i, 2:5] != 100)
            choice = random.randint(0, 3)
            while r[i][choice+2] == -100:
               choice = random.randint(0, 3)

            if choice == 0:
                row = row - 1
            elif choice == 1:
                col = col - 1
            elif choice == 2:
                row = row + 1
            elif choice == 3:
                col = col + 1

            i_next = find(row, col, r)
            q[i][choice] = q[i][choice] + alpha * (r[i_next][6] + belta * max(q[i_next][0], q[i_next][1], q[i_next][2], q[i_next][3]) - q[i][choice])
            i = i_next
            times = times + 1
        print(loop, times)
    print("done")


def qlearning_findroad(x):
    global q, r
    path = []
    position_x = position_y = 1
    while (position_x != x.shape[0]-2) or (position_y != x.shape[1]-2):
        path.append([position_x, position_y])
        ind = find(position_x, position_y, r)

        direction = argmax(q[ind, :-1])
        if direction == 0:
            position_x = position_x - 1
        if direction == 1:
            position_y = position_y - 1
        if direction == 2:
            position_x = position_x + 1
        if direction == 3:
            position_y = position_y + 1
        print(position_x, position_y)
    path.append([x.shape[0]-2, x.shape[1]-2])
    return path
