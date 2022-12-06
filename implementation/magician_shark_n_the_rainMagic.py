from collections import deque
import sys
import copy

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

move_info = deque()

for i in range(m):
    d,s = map(int,input().split())
    move_info.append((d-1,s))

has_cloud = [[0]*n for _ in range(n)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

for i in range(n-2,n):
    for j in range(0,2):
        has_cloud[i][j] = 1

while(move_info):
    dir,move = move_info.popleft()
    is_cloud = 0
    new_cloud = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if has_cloud[i][j]:
                ni = i + move*dx[dir]
                nj = j + move*dy[dir]
                if ni >= 0:
                    ni %= n
                elif ni < 0:
                    ni = n + (ni%n)
                    ni %= n
                if nj >= 0:
                    nj %= n
                elif nj < 0:
                    nj = n + (nj%n)
                    nj %= n
                new_cloud[ni][nj] = 1  # 구름이 중복 처리될 수 도 있다.
                matrix[ni][nj] += 1

    for i in range(n):
        for j in range(n):
            if new_cloud[i][j]:

                diagonal_cnt = 0

                for k in range(1,8,2):
                    di = i + dx[k]
                    dj = j + dy[k]
                    if 0<=di<n and 0<=dj<n and matrix[di][dj]:
                        diagonal_cnt += 1
                
                matrix[i][j] += diagonal_cnt
    
    new_new_cloud = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j]>=2 and not new_cloud[i][j]:
                matrix[i][j] -= 2
                new_new_cloud[i][j] = 1
    
    has_cloud = copy.deepcopy(new_new_cloud)

cnt_water = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            cnt_water += matrix[i][j]

print(cnt_water)