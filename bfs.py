import queue
import numpy as np
import stack


def searchNeighbours(i, j, x, Pass):
    neighbours = []
    if Pass[i, j + 1] == 0 and x[i, j + 1] == 0:
        neighbours.append([i, j + 1])
        Pass[i, j + 1] = 1

    if Pass[i + 1, j] == 0 and x[i + 1, j] == 0:
        neighbours.append([i + 1, j])
        Pass[i + 1, j] = 1

    if Pass[i - 1, j] == 0 and x[i - 1, j] == 0:
        neighbours.append([i - 1, j])
        Pass[i - 1, j] = 1

    if Pass[i, j - 1] == 0 and x[i, j - 1] == 0:
        neighbours.append([i, j - 1])
        Pass[i, j - 1] = 1

    return neighbours


def bfs(starti, startj, endi, endj, x):
    Pass = np.zeros((endj + 2, endi + 2), dtype=int)
    # print(Pass)
    pathQueue = queue.Queue(maxsize=0)
    temqueue = []
    allqueue = []

    pathQueue.put([starti, startj])

    end = False

    while not pathQueue.empty():

        coord = pathQueue.get()
        allqueue.append(coord)
        # print(coord)
        neighbours = searchNeighbours(coord[0], coord[1], x, Pass)
        for neighbour in neighbours:
            pathQueue.put(neighbour)
            if not end:
                temqueue.append([neighbour[0], neighbour[1]])
                temqueue.append([coord[0], coord[1]])  # 自己和父节点
            if [neighbour[0], neighbour[1]] == [endj, endi]:
                end = True
        if coord == [endj, endi]:
            break
            # return temqueue
    path = stack.Stack()
    path.push([endj, endi])
    temp = temqueue[len(temqueue) - 1]
    while temp != [starti, startj]:
        # print(temp)
        path.push(temp)
        for i in range(0, len(temqueue), 2):
            if temqueue[i] == temp:
                temp = temqueue[i + 1]

                break
    path.push([startj, starti])
    return path, allqueue

