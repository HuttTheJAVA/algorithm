from collections import deque
import sys
input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())

matrix = []

def switch_dice(dir,dice):
    dice_tmp = [0]*6
    if dir == 1:
        dice_tmp[1] = dice[0]
        dice_tmp[5] = dice[1]
        dice_tmp[2] = dice[2]
        dice_tmp[3] = dice[3]
        dice_tmp[0] = dice[4]
        dice_tmp[4] = dice[5]
    elif dir == 2:
        dice_tmp[4] = dice[0]
        dice_tmp[0] = dice[1]
        dice_tmp[2] = dice[2]
        dice_tmp[3] = dice[3]
        dice_tmp[5] = dice[4]
        dice_tmp[1] = dice[5]
    elif dir == 3:
        dice_tmp[3] = dice[0]
        dice_tmp[1] = dice[1]
        dice_tmp[0] = dice[2]
        dice_tmp[5] = dice[3]
        dice_tmp[4] = dice[4]
        dice_tmp[2] = dice[5]
    elif dir == 4:
        dice_tmp[2] = dice[0]
        dice_tmp[1] = dice[1]
        dice_tmp[5] = dice[2]
        dice_tmp[0] = dice[3]
        dice_tmp[4] = dice[4]
        dice_tmp[3] = dice[5]
    return dice_tmp

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

dir_lst = list(map(int,input().split()))

dice = [0,0,0,0,0,0]

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

for dir in dir_lst:
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0<=nx<n and 0<=ny<m:
        dice = switch_dice(dir,dice)
        if matrix[nx][ny]:
            dice[5] = matrix[nx][ny]
            matrix[nx][ny] = 0
        else:
            matrix[nx][ny] = dice[5]
        print(dice[0])
        x = nx 
        y = ny