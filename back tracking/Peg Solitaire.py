import sys
import copy
input = sys.stdin.readline

n = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs_peg(matrix,cnt,pin_cnt):
    global min_move
    global left_pin
    good_to_go = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'o':
                for idx in range(4):
                    ni = i + dx[idx]
                    nj = j + dy[idx]
                    ni2 = i + 2*dx[idx]
                    nj2 = j + 2*dy[idx]
                    if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj] == 'o':
                        if 0<=ni2<len(matrix) and 0<=nj2<len(matrix[0]) and matrix[ni2][nj2] == '.':
                            good_to_go = True
                            tmp_matrix = copy.deepcopy(matrix)
                            tmp_matrix[ni][nj] = '.'
                            tmp_matrix[ni2][nj2] = 'o'
                            tmp_matrix[i][j] = '.'
                            dfs_peg(tmp_matrix,cnt+1,pin_cnt-1)

    if not good_to_go:
        if pin_cnt<left_pin:
            left_pin = pin_cnt
            min_move = cnt


for t in range(n):
    matrix = []
    min_move = sys.maxsize
    for i in range(5):
        matrix.append(list(input().strip()))
    if t<n-1:
        input()
    pin_cnt = 0
    left_pin = sys.maxsize
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'o':
                pin_cnt += 1
    
    dfs_peg(matrix,0,pin_cnt)
    print(left_pin,min_move)