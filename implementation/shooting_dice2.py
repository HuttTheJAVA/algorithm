from collections import deque
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

def rearrange_dice(dice,dir):
    new_dice = [0]*len(dice)
    if dir == 0:
        new_dice[0] = dice[3]
        new_dice[1] = dice[0]
        new_dice[2] = dice[2]
        new_dice[3] = dice[5]
        new_dice[4] = dice[4]
        new_dice[5] = dice[1]
    elif dir == 1:
        new_dice[0] = dice[2]
        new_dice[1] = dice[1]
        new_dice[2] = dice[5]
        new_dice[3] = dice[3]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]
    elif dir == 2:
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[2]
        new_dice[3] = dice[0]
        new_dice[4] = dice[4]
        new_dice[5] = dice[3]
    elif dir == 3:
        new_dice[0] = dice[4]
        new_dice[1] = dice[1]
        new_dice[2] = dice[0]
        new_dice[3] = dice[3]
        new_dice[4] = dice[5]
        new_dice[5] = dice[2]
    
    return new_dice

def change_dice_dir(dir,clock_wise):
    if clock_wise:
        dir += 1
        if dir == 4:
            dir = 0
    else:
        dir -= 1
        if dir < 0:
            dir = 3
    
    return dir
        
dice = [1,3,2,4,5,6]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

x = 0
y = 0

dir = 0

score = 0
move_cnt = 0
while(move_cnt<k):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0<=nx<n and 0<=ny<m:
        move_cnt+=1
        dice = rearrange_dice(dice,dir)
        under_number = dice[5]
        x = nx
        y = ny
        qu = deque()
        qu.append((x,y))
        visit = [[0]*m for i in range(n)]
        visit[x][y] = 1
        score += matrix[x][y]

        while(qu):
            now_x,now_y = qu.popleft()
            for i in range(4):
                next_x = now_x + dx[i]
                next_y = now_y + dy[i]
                if 0<=next_x<n and 0<=next_y<m and not visit[next_x][next_y] and matrix[next_x][next_y] == matrix[x][y]:
                    score += matrix[next_x][next_y]
                    visit[next_x][next_y] = 1
                    qu.append((next_x,next_y))
        
        if under_number > matrix[x][y]:
            dir = change_dice_dir(dir,1)
        elif under_number < matrix[x][y]:
            dir = change_dice_dir(dir,0)

    else:
        dir = (dir+2)%4

print(score)