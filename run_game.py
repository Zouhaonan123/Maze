import sys
import pygame
import human_move
import dfs_move
import random_maze
import bfs_move
import qlearning_move
import  antcolony_move
import screen_init
import qlearning
from button import Button
import threading


width = 21 # 迷宫宽度
height = 19 # 迷宫高度
grid = 30 # 单元格边长

# 各按钮颜色
button1_color = [0, 250, 0]
button2_color = [0, 255, 0]
button3_color = [0, 255, 0]
button4_color = [0, 255, 0]
button5_color = [0, 255, 0]
button6_color = [0, 255, 0]
button7_color = [0, 255, 0]

# 各按钮上文字颜色
button1_text_color = [0, 0, 255]
button2_text_color = [0, 0, 255]
button3_text_color = [0, 0, 255]
button4_text_color = [0, 0, 255]
button5_text_color = [0, 0, 255]
button6_text_color = [0, 0, 255]
button7_text_color = [0, 0, 255]


starti = 1
startj = 1


def run_game():

    q_thread = []
    i = -1 # 线程序号
    learned = False

    pygame.init()

    image_Mario = pygame.image.load('images/Mario.bmp')
    Mario_Rect = image_Mario.get_rect()
    image_Ground = pygame.image.load('images/Ground.bmp')
    Ground_Rect = image_Ground.get_rect()

    if height <= 20:
        screen = pygame.display.set_mode((width * grid + 200, 600))
    else:
        screen = pygame.display.set_mode((width * grid + 300, height * grid))
    screen.fill([0, 191, 255])
    pygame.display.set_caption("迷宫小游戏^_^")
    pygame.display.flip()

    game_states = 0
    button1 = Button(screen, "play myself", width * grid + 100, 200, button1_color, button1_text_color)
    button2 = Button(screen, "DFS", width * grid + 100, 280, button2_color, button2_text_color)
    button3 = Button(screen, "BFS", width * grid + 100, 360, button3_color, button3_text_color)
    button4 = Button(screen, "Q-Learning", width * grid + 100, 440, button4_color, button4_text_color)
    button5 = Button(screen, "Ant colony", width * grid + 100, 520, button5_color, button5_text_color)
    button6 = Button(screen, "change map", width * grid + 100, 120, button6_color, button6_text_color)
    button7 = Button(screen, "display", width * grid + 100, 440, button7_color, button7_text_color)

    x = random_maze.prim_maze(width, height)
    screen_init.screen_init(screen, image_Ground, Ground_Rect, x, grid)
    pygame.display.flip()
    while True:

        if not game_states:

            button1.draw_button()
            button2.draw_button()
            button3.draw_button()
            button5.draw_button()
            if i < 0 or not q_thread[i].is_alive():
                button6.draw_button()
            if not learned:
                button4.draw_button()
            elif learned:
                button7 = Button(screen, "display", width * grid + 100, 440, button7_color, button7_text_color)
                button7.draw_button()

        pygame.display.flip()
        flag = True

        while flag:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if button1.rect.collidepoint(mouse_x, mouse_y):
                        game_states = 1
                        flag = False
                    elif button2.rect.collidepoint(mouse_x, mouse_y):
                        game_states = 2
                        flag = False
                    elif button3.rect.collidepoint(mouse_x, mouse_y):
                        game_states = 3
                        flag = False
                    elif button4.rect.collidepoint(mouse_x, mouse_y) and button4.exist:  # 学习
                        i = i + 1
                        t = threading.Thread(target=qlearning.qlearning_learning, args=(x,))
                        q_thread.append(t)
                        q_thread[i].start()
                        button4.delete()
                        button6.delete()
                        learned = True
                        flag = False
                    elif button5.rect.collidepoint(mouse_x, mouse_y):
                        game_states = 5
                        flag = False

                    elif button6.rect.collidepoint(mouse_x, mouse_y) and button6.exist:  # 改地图
                        x = random_maze.prim_maze(width, height)
                        button7.delete()
                        learned = False
                        flag = False

                    elif button7.rect.collidepoint(mouse_x, mouse_y) and button7.exist:  # 生成路径
                        if not q_thread[i].is_alive():
                            game_states = 4
                        flag = False

        screen_init.screen_init(screen, image_Ground, Ground_Rect, x, grid)
        pygame.display.flip()
        if game_states == 1:
            human_move.move(screen, x, image_Mario, Mario_Rect, image_Ground, Ground_Rect, grid)
            game_states = 0
        elif game_states == 2:
            dfs_move.dfs_move(screen, x, image_Mario, Mario_Rect, image_Ground, Ground_Rect, width, height, grid, starti, startj)
            game_states = 0
        elif game_states == 3:
            bfs_move.bfs_move(screen, x, image_Mario, Mario_Rect, image_Ground, Ground_Rect, width, height, grid, starti, startj)
            game_states = 0
        elif game_states == 4:
            qlearning_move.qlearning_move(screen, x, image_Mario, Mario_Rect, image_Ground, Ground_Rect, grid)
            game_states = 0
        elif game_states == 5:
            antcolony_move.antcolony_move(screen, x, image_Mario, Mario_Rect, image_Ground, Ground_Rect, grid, starti, startj)
            game_states = 0


run_game()