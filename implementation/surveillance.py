from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def switch_dir(dir):
    if dir<0:
        dir = 3
    if dir>3:
        dir = 0

    return dir

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

cctv_order_x_y = []

cctv_order_kind = []

cnt = 643634

cctv_dir_dct = {1:[0,1,2,3],2:[0,1],3:[0,1,2,3],4:[0,1,2,3],5:[0]}

def bfs(next_x,next_y):
    global matrix
    if 0<=next_x<n and 0<=next_y<m and matrix[next_x][next_y] != 6:
        if not matrix[next_x][next_y]:
            matrix[next_x][next_y] = '#'
        x = next_x
        y = next_y
    else:
        return None,None
    return x,y

cctv_is_five = []

for i in range(n):
    for j in range(m):
        if 1<=matrix[i][j]<5:
            cctv_order_x_y.append((i,j))
            cctv_order_kind.append(matrix[i][j])
        elif matrix[i][j] == 5:
            cctv_is_five.append((i,j))

for cctv_5 in cctv_is_five:
    x = cctv_5[0]
    y = cctv_5[1]
    init_x = x
    init_y = y
    for i in range(4):
        while(1):
            next_x = x + dx[i]
            next_y = y + dy[i]
            x,y = bfs(next_x,next_y)
            if x == None and y == None:
                break
        x = init_x
        y = init_y

qu = deque()

if cctv_order_kind:

    for dir in cctv_dir_dct[cctv_order_kind[0]]:
        qu.append(str(dir))

    for ki in range(1,len(cctv_order_kind)):
        new_qu = deque()
        while(qu):
            combi = qu.popleft()
            for dir in cctv_dir_dct[cctv_order_kind[ki]]:
                new_combi = combi + str(dir)
                new_qu.append(new_combi)
        qu = new_qu

    tmp = [[0]*m for i in range(n)]

    for i in range(n):
        for j in range(m):
            tmp[i][j] = matrix[i][j]

    while(qu):
        for i in range(n):
            for j in range(m):
                matrix[i][j] = tmp[i][j]

        combi = qu.popleft()

        for idx in range(len(combi)): ### combi = dir combi = 동 서 남 남 서 북 ...
            x = cctv_order_x_y[idx][0]
            y = cctv_order_x_y[idx][1]
            init_x = x 
            init_y = y
            cctv_kind = cctv_order_kind[idx]
            direction = int(combi[idx])
            if cctv_kind == 1:
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
            elif cctv_kind == 2:
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
                direction = switch_dir(direction+2)
                x = init_x
                y = init_y
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
            elif cctv_kind == 3:
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
                direction = switch_dir(direction-1)
                x = init_x
                y = init_y
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
            elif cctv_kind == 4:
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
                direction = switch_dir(direction-1)
                x = init_x
                y = init_y
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
                direction = switch_dir(direction-1)
                x = init_x
                y = init_y
                while(1):
                    next_x = x + dx[direction]
                    next_y = y + dy[direction]
                    x,y = bfs(next_x,next_y)
                    if x == None and y == None:
                        break
        cnt_blind_spot = 0
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    cnt_blind_spot += 1
        cnt = min(cnt,cnt_blind_spot)

else:
    cnt_blind_spot = 0
    for i in range(n):
        for j in range(m):
            if not matrix[i][j]:
                cnt_blind_spot += 1
    cnt = min(cnt,cnt_blind_spot)
    

print(cnt)