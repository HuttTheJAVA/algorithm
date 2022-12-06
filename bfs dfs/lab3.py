from collections import deque
import heapq
from itertools import combinations
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

qu = deque()

series_number = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            qu.append((i,j,series_number))
            series_number += 1

virus_cnt = len(qu)

shortest_virus_matrix = [[[sys.maxsize]*virus_cnt for i in range(n)] for j in range(n)]

for virus in qu:
    shortest_virus_matrix[virus[0]][virus[1]][virus[2]] = 0

while(qu):
    x,y,series_num = qu.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<n and 0<=ny<n and matrix[nx][ny] != 1 and shortest_virus_matrix[nx][ny][series_num] > shortest_virus_matrix[x][y][series_num] + 1:
            shortest_virus_matrix[nx][ny][series_num] = shortest_virus_matrix[x][y][series_num] + 1
            qu.append((nx,ny,series_num))

total_max_time = sys.maxsize

for virus_lst in combinations([i for i in range(virus_cnt)],m):
    max_time = 0
    for i in range(n):
        for j in range(n):
            if not matrix[i][j]:
                min_time = sys.maxsize
                for number in virus_lst:
                    min_time = min(min_time,shortest_virus_matrix[i][j][number])
                max_time = max(max_time,min_time)
    total_max_time = min(total_max_time,max_time)

if total_max_time != sys.maxsize:
    print(total_max_time)
else:
    print(-1)