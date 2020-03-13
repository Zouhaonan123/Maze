import numpy as np
import random
import stack
import math
import copy


class Point:
    x = 0
    y = 0

    def __init__(self):
        self.x = 0
        self.y = 0

    def setpoint(self, x, y):
        self.x = x
        self.y = y

class Map:
    row: int = 0
    col: int = 0
    p = []
    starti = 0
    startj = 0
    endi = 0
    endj = 0
    around = []

    def __init__(self, p, row, col, starti, startj, endi, endj):
        self.p = copy.deepcopy(p)
        self.row = row
        self.col = col
        self.starti = starti
        self.startj = startj
        self.endi = endi
        self.endj = endj
        self.around = np.zeros((row, col, 4), dtype=np.int)

solution = 0


def findpath(map):
    road = []
    N1 = map.row
    N2 = map.col

    numberofAnts = 10  # number of ants
    rcmax = 200
    IN = 1

    add = np.zeros((N1, N2), dtype=np.float) # 信息素增量
    phe = np.zeros((N1, N2), dtype=np.float) # 信息素
    MAX = 0x3f3f3f3f

    alphe = beta = 2
    rout = 0.7
    Q = 10
    #  alphe信息素的影响因子，betra路线距离的影响因子，rout信息素的保持度，Q用于计算每只蚂蚁在其路迹留下的信息素增量
    bestsolution = MAX

    bestpath = stack.Stack()

    for i in range(0, N1):
        for j in range(0, N2):
            phe[i][j] = IN

    offset = []
    for i in range(0, 4):
        temp = Point()
        offset.append(temp)
    offset[0].setpoint(0, 1)
    offset[1].setpoint(1, 0)
    offset[2].setpoint(0, -1)
    offset[3].setpoint(-1, 0)

    # 每一只蚂蚁走过的路，用于每一只蚂蚁来更新信息素
    stackpath = []
    for i in range(0, numberofAnts):
        temp = stack.Stack()
        stackpath.append(temp)
    # 障碍地图，禁忌表
    Ini_map = []
    for i in range(0, numberofAnts):
        temp = Map(map.p, map.row, map.col, map.starti, map.startj, map.endi, map.endj)
        Ini_map.append(temp)
    # 记录每一只🐜的当前位置，用于最后记录路径
    allposition = []
    for i in range(0, numberofAnts):
        temp = Point()
        allposition.append(temp)

    # 循环轮次
    s = 0
    while s < rcmax:
        for i in range(0, numberofAnts):
            while not stackpath[i].is_empty():
                stackpath[i].pop()
        for i in range(0, numberofAnts):
            Ini_map[i] = copy.deepcopy(map)
            Ini_map[i].p[map.starti][map.startj] = 1
            stackpath[i].push([map.starti, map.startj])
            allposition[i].setpoint(map.starti, map.startj)
        # 开始蚂蚁循环
        for j in range(0, numberofAnts):
            while (allposition[j].x != map.endi) | (allposition[j].y != map.endj):
                psum: float = 0.0

                for op in range(0, 4):
                    x = allposition[j].x + offset[op].x
                    y = allposition[j].y + offset[op].y

                    if (Ini_map[j].around[allposition[j].x][allposition[j].y][op] == 0) & (Ini_map[j].p[x][y] != 1):
                        psum += (math.pow(phe[x][y], alphe) * math.pow(10.0 / stackpath[j].size(), beta))

                if psum != 0:
                    drand = random.random()  # 轮盘赌随机选择一个点（较大概率选择随机，而非直接选择最大概率）
                    pro = 0.0
                    for re in range(0, 4):
                        # nonlocal x_in, y_in
                        x_in = allposition[j].x + offset[re].x
                        y_in = allposition[j].y + offset[re].y
                        if (Ini_map[j].around[allposition[j].x][allposition[j].y][re] == 0) & (Ini_map[j].p[x_in][y_in] != 1):
                            pro += ((math.pow(phe[x_in][y_in], alphe) * math.pow(10.0 / stackpath[j].size(), beta)) / psum)
                            if pro >= drand:  # 轮盘赌选择成功，退出，当前点为选择点
                                break
                    # 蚂蚁选择改点
                    allposition[j].x = x_in
                    allposition[j].y = y_in
                    stackpath[j].push([allposition[j].x, allposition[j].y])
                    # 设置障碍
                    Ini_map[j].p[allposition[j].x][allposition[j].y] = 1
                else:  # 没找到下一点
                    stackpath[j].pop()  # 向后退一步，出栈
                    Ini_map[j].p[allposition[j].x][allposition[j].y] = 0
                    if stackpath[j].is_empty():
                        return False
                    # 设置回溯后的Allposition
                    if allposition[j].x == stackpath[j].peek()[0]:
                        if allposition[j].y - stackpath[j].peek()[1] == 1:  # 👉
                            Ini_map[j].around[stackpath[j].peek()[0]][stackpath[j].peek()[1]][0] = 1  # 标记该方向被访问过
                        if allposition[j].y - stackpath[j].peek()[1] == -1:  # 👈
                            Ini_map[j].around[stackpath[j].peek()[0]][stackpath[j].peek()[1]][2] = 1
                    if allposition[j].y == stackpath[j].peek()[1]:
                        if allposition[j].x - stackpath[j].peek()[0] == 1:  # 👇
                            Ini_map[j].around[stackpath[j].peek()[0]][stackpath[j].peek()[1]][1] = 1
                        if allposition[j].x - stackpath[j].peek()[0] == -1:  # 👆
                            Ini_map[j].around[stackpath[j].peek()[0]][stackpath[j].peek()[1]][3] = 1
                    allposition[j].x = stackpath[j].peek()[0]
                    allposition[j].y = stackpath[j].peek()[1]

        # 保存最优路径
        global solution
        solution = 0
        for i in range(0, numberofAnts):
            solution = stackpath[i].size()
            if solution < bestsolution:
                bestpath = copy.deepcopy(stackpath[i])
                bestsolution = solution

        for i in range(0, N1):
            for j in range(0, N2):
                add[i][j] = 0

        for i in range(0, numberofAnts):
            solu = stackpath[i].size()
            d = Q / solu  # Q为10，增量d = 蚂蚁数/路径长度
            while not stackpath[i].is_empty(): # 只对走过的路进行增加信息素
                add[stackpath[i].peek()[0]][stackpath[i].peek()[1]] += d
                stackpath[i].pop()
        for i in range(0, N1):
            for j in range(0, N2):
                phe[i][j] = phe[i][j] * rout + add[i][j] # 乘上挥发系数，再加上信息素增量

                if phe[i][j] < 0.0001:
                    phe[i][j] = 0.0001
                if phe[i][j] > 20:
                    phe[i][j] = 20
        s += 1

    while not bestpath.is_empty():
        road.insert(0, [bestpath.peek()[0], bestpath.peek()[1]])
        bestpath.pop()

    return road















