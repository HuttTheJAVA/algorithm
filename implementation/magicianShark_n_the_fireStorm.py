import sys
from collections import deque
input = sys.stdin.readline

n,q = map(int,input().split())

size = 2**n

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(size):
    matrix.append(list(map(int,input().split())))

stage_lst = list(map(int,input().split()))

def clock_wise_90(start_row,end_row,start_col,end_col):  # 이 matrix 는 조각처리된 매트릭스여야한다.
    global matrix
    tmp_matrix = [[0]*(end_col-start_col) for i in range(start_row,end_row)]

    for i in range(start_row,end_row):
        for j in range(start_col,end_col):
            tmp_matrix[j-start_col][(end_row-1)-i] = matrix[i][j]
    
    for i in range(start_row,end_row):
        for j in range(start_col,end_col):
            matrix[i][j] = tmp_matrix[i-start_row][j-start_col]

for idx in range(q):
    stride = 2**stage_lst[idx]
    if stride > 1:
        for i in range(0,size,stride):
            for j in range(0,size,stride):
                clock_wise_90(i,i+stride,j,j+stride)
    
    melt_x_y = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]:
                cnt_adj = 0
                for dir in range(4):
                    ni = i + dx[dir]
                    nj = j + dy[dir]
                    if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj]:
                        cnt_adj += 1
                if cnt_adj < 3:
                    melt_x_y.append((i,j))
    
    for x_y in melt_x_y:
        matrix[x_y[0]][x_y[1]] -= 1


max_mass = 0
total_ice = 0

visit = [[0]*len(matrix[0]) for i in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] and not visit[i][j]:
            qu = deque()
            qu.append((i,j))
            mass = 1
            total_ice += matrix[i][j]
            visit[i][j] = 1
            while(qu):
                x,y = qu.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and matrix[nx][ny] and not visit[nx][ny]:
                        qu.append((nx,ny))
                        mass += 1
                        visit[nx][ny] = 1
                        total_ice += matrix[nx][ny]
            max_mass = max(max_mass,mass)
print(total_ice)
print(max_mass)
