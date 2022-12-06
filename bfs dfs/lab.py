from collections import deque
import sys
import copy
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

virus_x_y = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_zero_cnt = 0
def install_wall(cnt,start_row):
    global matrix
    global virus_x_y
    global nx
    global ny
    global max_zero_cnt
    if cnt == 3:
        tmp_matrix = copy.deepcopy(matrix)
        qu = deque()
        for x_y in virus_x_y:
            qu.append((x_y[0],x_y[1]))
        while(qu):
            x,y = qu.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m and not tmp_matrix[nx][ny]:
                    tmp_matrix[nx][ny] = 2
                    qu.append((nx,ny))
        cnt_zero = 0
        for i in range(n):
            for j in range(m):
                if not tmp_matrix[i][j]:
                    cnt_zero += 1
        max_zero_cnt = max(max_zero_cnt,cnt_zero)
        return
    
    for i in range(start_row,n):
        for j in range(m):
            if not matrix[i][j]:
                matrix[i][j] = 1
                install_wall(cnt+1,i)
                matrix[i][j] = 0
 




for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus_x_y.append((i,j))

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            matrix[i][j] = 1
            install_wall(1,i)
            matrix[i][j] = 0
print(max_zero_cnt)