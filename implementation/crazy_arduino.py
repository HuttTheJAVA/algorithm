from collections import deque
import sys
input = sys.stdin.readline

r,c = map(int,input().split())

matrix = []

crazy_Arduino = []

overlap_x_y = {}

x = None
y = None

res = 'ABC'

dx = [None,1,1,1,0,0,0,-1,-1,-1]
dy = [None,-1,0,1,-1,0,1,-1,0,1]

for i in range(r):
    matrix.append(list(input().strip()))

movements = list(map(int,list(input().strip())))

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'I':
            x = i
            y = j
        elif matrix[i][j] == 'R':
            crazy_Arduino.append((i,j))
            overlap_x_y[(i,j)] = 1

for i in range(len(movements)):
    if res != 'ABC':
        break
    nx = x + dx[movements[i]]
    ny = y + dy[movements[i]]
    if (nx,ny) in overlap_x_y:
        res = i
        break
    x = nx
    y = ny
    to_append_in_overlap_x_y = []
    new_dct = {}
    for coor in overlap_x_y.keys():
        x_gap = 1000
        y_gap = 1000
        temp_x = coor[0]
        temp_y = coor[1]
        min_idx = None
        overlap_x_y[coor[0],coor[1]] -= 1
        
        for idx in range(1,len(dx)):
            n_coor_x = temp_x+dx[idx]
            n_coor_y = temp_y+dy[idx]
            if 0<=n_coor_x<r and 0<=n_coor_y<c:
                if x_gap+y_gap > abs(x-n_coor_x)+abs(y-n_coor_y):
                    x_gap = abs(x-n_coor_x)
                    y_gap = abs(y-n_coor_y)
                    min_idx = idx
                    if not(x_gap+y_gap):
                        res = i
                        break
        if (temp_x+dx[min_idx],temp_y+dy[min_idx]) in overlap_x_y:  ###????????????????????
            overlap_x_y[temp_x+dx[min_idx],temp_y+dy[min_idx]] += 1
        else:
            if (temp_x+dx[min_idx],temp_y+dy[min_idx]) in new_dct:
                new_dct[temp_x+dx[min_idx],temp_y+dy[min_idx]] += 1
            else:
                new_dct[temp_x+dx[min_idx],temp_y+dy[min_idx]] = 1
    final_dct = {}
    for i in overlap_x_y.keys():
        if overlap_x_y[i] == 1:
            final_dct[i] = 1
    for i in new_dct.keys():
        if new_dct[i] == 1:
            final_dct[i] = 1

    overlap_x_y = final_dct

if res == "ABC":
    matrix = [['.']*c for i in range(r)]
    matrix[x][y] = 'I'
    for i in overlap_x_y.keys():
        matrix[i[0]][i[1]] = 'R'
    
    for i in range(len(matrix)):
        word = ''
        for j in range(len(matrix[0])):
            word += matrix[i][j]
        print(word)
else:
    print(f"kraj {res+1}")