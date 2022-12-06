from collections import deque
import heapq
import sys
input = sys.stdin.readline

matrix = []

for i in range(9):
    matrix.append(list(map(int,input().split())))

zero_cnt = 0

zero_x_y = []

for i in range(9):
    for j in range(9):
        if not matrix[i][j]:
            zero_cnt+=1
            zero_x_y.append((i,j))

back = False

def dfs(i,j,zero_idx):
    global matrix
    global zero_cnt
    global back
    if back:
        return
    p_i = i//3
    p_j = j//3
    number_lst = [0]*(10)
    for idx in range(3*p_i,3*p_i+3):
        for jdx in range(3*p_j,3*p_j+3):
            if matrix[idx][jdx]:
                number_lst[matrix[idx][jdx]] = 1
    for jdx in range(9):
        if matrix[i][jdx]:
            number_lst[matrix[i][jdx]] = 1
    
    for idx in range(9):
        if matrix[idx][j]:
            number_lst[matrix[idx][j]] = 1
    
    for num in range(1,10):
        if not number_lst[num]:
            matrix[i][j] = num
            zero_cnt -= 1
            if not zero_cnt:
                back = True
                for line in matrix:
                    print(*line)
                return
            dfs(zero_x_y[zero_idx+1][0],zero_x_y[zero_idx+1][1],zero_idx+1)
            zero_cnt += 1
            matrix[i][j] = 0
    

dfs(zero_x_y[0][0],zero_x_y[0][1],0)