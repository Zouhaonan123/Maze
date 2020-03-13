import numpy as np
import stack

findResult: bool = False
time = 1
this_time = False
def findpath(starti, startj, endj, endi, x):
    path = stack.Stack()
    path.push([1, 1])
    road = stack.Stack()
    #print(path.pop())

    Pass = np.zeros((endi + 2, endj + 2), dtype=int)


    def dfs(i, j):
        Pass[i, j] = 1
        global this_time
        this_time = False
        global findResult
        if (i, j) == (endi, endj):
            findResult = True
        if findResult:
            #print("结束")
            for times in range(path.size()):
                road.push(path.pop())
            findResult = False
            return
        if Pass[i, j + 1] == 0 and x[i, j + 1] == 0:
            path.push([i, j + 1])
            dfs(i, j + 1)
            this_time = True

        if Pass[i + 1, j] == 0 and x[i + 1, j] == 0:
            if this_time:
                path.push([i, j])
            path.push([i + 1, j])
            dfs(i + 1, j)
            this_time = True

        if Pass[i - 1, j] == 0 and x[i - 1, j] == 0:
            if this_time:
                path.push([i, j])
            path.push([i - 1, j])
            dfs(i - 1, j)
            this_time = True

        if Pass[i, j - 1] == 0 and x[i, j - 1] == 0:
            if this_time:
                path.push([i, j])
            path.push([i, j - 1])
            dfs(i, j - 1)
            this_time = True

        if path.size() != 0:
            path.push([i, j])
            # path.pop()
            pass
    dfs(starti, startj)
    return road


