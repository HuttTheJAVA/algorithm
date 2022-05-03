import sys
input = sys.stdin.readline

n,m = map(int,input().split())

num = int(input())

def direct(idx):  # 방향을 바꿔주는 함수 return 인덱스
    if idx == 4:
        idx = 0
    return idx

matrix = [[-1]*n for i in range(m)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

x,y = m-1,0

i = 0

val = 1

if val == num:
    x_y = [y+1,m-x]
else:
    x_y = []

matrix[x][y] = val

val += 1


while(1):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<m and 0<=ny<n:
        if matrix[nx][ny] != -1:
            i = direct(i+1)

        else:
            matrix[nx][ny] = val
            if val == num:
                x_y.append(ny+1)
                x_y.append(m - nx)
            val += 1
            x = nx
            y = ny
            if val>n*m:
                break
    else:
        i = direct(i+1)

if x_y:
    print(*x_y)
else:
    print(0)
