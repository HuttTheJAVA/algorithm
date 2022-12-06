from collections import deque
import sys

input = sys.stdin.readline

puyo = []

for i in range(12):
    puyo.append(list(input().strip()))

row = 12
col = 6

dx = [0,1,0,-1]
dy = [1,0,-1,0]

chain_react = 0

def gravity(matrix):
    dx = 1
    dy = 0
    for i in range(len(matrix)-2,-1,-1):
        for j in range(len(matrix[0])):
            if matrix[i][j] != '.':
                changable_i = i
                changable_j = j
                while(1):
                    ni = changable_i + dx
                    nj = changable_j + dy
                    if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj] == '.':
                        changable_i = ni
                        changable_j = nj
                    else:
                        break
                if i != changable_i or j != changable_j:
                    matrix[changable_i][changable_j] = matrix[i][j]
                    matrix[i][j] = '.'
    
    return matrix


while(1):
    visit = [[0]*col for i in range(row)]
    puyo_group_lst = []
    group_made = 0
    for i in range(row):
        for j in range(col):
            if puyo[i][j] != '.' and not visit[i][j]:
                small_group = [(i,j)]
                qu = deque()
                qu.append((i,j))
                visit[i][j] = 1
                while(qu):
                    x,y = qu.popleft()
                    for idx in range(4):
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if 0<=nx<row and 0<=ny<col and not visit[nx][ny] and puyo[x][y] == puyo[nx][ny]:
                            visit[nx][ny] = 1
                            small_group.append((nx,ny))
                            qu.append((nx,ny))
                if len(small_group)>= 4:
                    group_made = 1
                    puyo_group_lst.append(small_group)
    if not group_made:
        break
    chain_react += 1
    for group in puyo_group_lst:
        for x_y in group:
            puyo[x_y[0]][x_y[1]] = '.'

    puyo = gravity(puyo)

print(chain_react)