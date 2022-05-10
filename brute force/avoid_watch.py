import sys
input = sys.stdin.readline

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(input().split()))

def detection(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    orgx = x
    orgy = y
    for i in range(4):
        x = orgx
        y = orgy
        while(1):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if matrix[nx][ny] == 'O':
                    break
                elif matrix[nx][ny] == 'S':
                    return False
                x = nx
                y = ny
            else:
                break
    return True

can = []

def plant_obstacle(cnt):
    global can
    if can:
        return 
    if cnt == 3:
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 'T':
                    if not detection(i,j):
                        return
        can = [True]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'X':
                matrix[i][j] = 'O'
                plant_obstacle(cnt+1)
                matrix[i][j] = 'X'

plant_obstacle(0)

if can:
    print('YES')
else:
    print('NO')