
import sys
import pygame
import screen_init
from scoreboard import Scoreboard


def move_update(rect, move_right, move_left, move_up, move_down, count0):
    if move_right:
        rect.centerx += 1
        count0 += 1
    elif move_left:
        rect.centerx -= 1
        count0 += 1
    elif move_up:
        rect.centery -= 1
        count0 += 1
    elif move_down:
        rect.centery += 1
        count0 += 1
    return count0


def move(screen, x, image1, rect1, image2, rect2, grid):
    pygame.key.set_repeat(200, 50)
    count = 0
    scoreboard = Scoreboard(screen, count)
    move_right = False
    move_left = False
    move_up = False
    move_down = False
    rect1.center = [grid+(grid/2), grid+(grid/2)]

    while True:

        screen_init.screen_init(screen, image2, rect2, x, grid)

        # 画出发点和终点
        pygame.draw.rect(screen, [0, 0, 255], [grid, grid, grid, grid], 0)
        pygame.draw.rect(screen, [255, 0, 0], [grid * (x.shape[1] - 2), grid * (x.shape[0] - 2), grid, grid], 0)

        # 判定撞墙
        if x[int((rect1.centery - (grid/2)) / grid)][int((rect1.centerx + (grid/2)) / grid)] == 1: # 右
            move_right = False

        if x[int((rect1.centery - (grid/2)) / grid)][int((rect1.centerx - (grid/2)) / grid)] == 1: # 左
            move_left = False

        if x[int((rect1.centery - (grid/2)) / grid)][int((rect1.centerx - (grid/2)) / grid)] == 1: # 上
            move_up = False

        if x[int((rect1.centery + (grid/2)) / grid)][int((rect1.centerx - (grid/2)) / grid)] == 1: # 下
            move_down = False

        count = move_update(rect1, move_right, move_left, move_up, move_down, count)

        score = int(count / grid)
        scoreboard.prep_count(score)
        screen.blit(image1, rect1)
        scoreboard.show_count()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_right = True

                elif event.key == pygame.K_LEFT:
                    move_left = True

                elif event.key == pygame.K_UP:
                    move_up = True

                elif event.key == pygame.K_DOWN:
                    move_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    move_right = False
                    flag = False
                    for m in range(1, x.shape[0]):
                        for n in range(1, x.shape[1]):
                            if (abs(rect1.centerx-grid*n-(grid/2)) <= (grid/2)) & (abs(rect1.centery-grid*m-(grid/2)) <= (grid/2)):
                                rect1.center = [grid*n+(grid/2), grid*m+(grid/2)]
                                flag = True
                        if flag:
                            break

                elif event.key == pygame.K_LEFT:
                    move_left = False
                    flag = False
                    for m in range(1, x.shape[0]):
                        for n in range(1, x.shape[1]):
                            if (abs(rect1.centerx - grid * n - (grid/2)) <= (grid/2)) & (abs(rect1.centery - grid * m - (grid/2)) <= (grid/2)):
                                rect1.center = [grid * n + (grid/2), grid * m + (grid/2)]
                                flag = True
                        if flag:
                            break

                elif event.key == pygame.K_UP:
                    move_up = False
                    flag = False
                    for m in range(1, x.shape[0]):
                        for n in range(1, x.shape[1]):
                            if (abs(rect1.centerx - grid * n - (grid/2)) <= (grid/2)) & (abs(rect1.centery - grid * m - (grid/2)) <= (grid/2)):
                                rect1.center = [grid * n + (grid/2), grid * m + (grid/2)]
                                flag = True
                        if flag:
                            break

                elif event.key == pygame.K_DOWN:
                    move_down = False
                    flag = False
                    for m in range(1, x.shape[0]):
                        for n in range(1, x.shape[1]):
                            if (abs(rect1.centerx - grid * n - (grid/2)) <= (grid/2)) & (abs(rect1.centery - grid * m - (grid/2)) <= (grid/2)):
                                rect1.center = [grid * n + (grid/2), grid * m + (grid/2)]
                                flag = True
                        if flag:
                            break

        if (int((rect1.centery - (grid/2)) / grid) == x.shape[0] - 2) & (int((rect1.centerx - (grid/2)) / grid) == x.shape[1] - 2):
            # print(x)
            break

    return True