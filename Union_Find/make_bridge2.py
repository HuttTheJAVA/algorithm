import sys
from collections import deque
input = sys.stdin.readline

def find_affiliation(x):
    global affiliation_island
    if affiliation_island[x] == x:
        return x
    affiliation_island[x] = find_affiliation(affiliation_island[x])
    return affiliation_island[x] 

def union_affiliation(x,y):
    global affiliation_island
    aff_x = find_affiliation(x)
    aff_y = find_affiliation(y)
    if aff_x == aff_y:
        return
    elif aff_x < aff_y:
        affiliation_island[aff_y] = aff_x
    else:
        affiliation_island[aff_x] = aff_y

n,m = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    matrix.append(list(map(int,input().split())))

island = 0

visit = [[0]*len(matrix[0]) for i in range(len(matrix))]

for i in range(n):
    for j in range(m):
        if matrix[i][j] and not visit[i][j]:
            qu = deque()
            qu.append((i,j))
            island += 1
            visit[i][j] = island
            while(qu):
                x,y = qu.popleft()
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and matrix[nx][ny]:
                        visit[nx][ny] = island
                        qu.append((nx,ny))

edges = []  # 시작 섬, 도착 섬, 다리 길이.

affiliation_island = [i for i in range(island+1)] # 소속 아일랜드

for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            start_island = visit[i][j]
            for idx in range(4):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if 0<=nx<n and 0<=ny<m and not matrix[nx][ny]:
                    bridge_len = 0
                    end_island = None
                    qu = deque()
                    qu.append((nx,ny))
                    bridge_len += 1
                    while(qu):
                        local_x,local_y = qu.popleft()
                        next_local_x = local_x + dx[idx]
                        next_local_y = local_y + dy[idx]
                        if 0<=next_local_x<n and 0<=next_local_y<m:
                            if not matrix[next_local_x][next_local_y]:
                                bridge_len += 1
                                qu.append((next_local_x,next_local_y))
                            elif visit[next_local_x][next_local_y] != start_island and bridge_len >= 2:
                                edges.append((start_island,visit[next_local_x][next_local_y],bridge_len))

total_bridge_len = 0

edges.sort(key=lambda x:(x[2],x[0],x[1]))

for edge in edges:
    start_island,end_island,bridge_len = edge
    aff_start = find_affiliation(start_island)
    aff_end = find_affiliation(end_island)
    if aff_start != aff_end:
        union_affiliation(aff_start,aff_end)
        total_bridge_len += bridge_len
        island -= 1

if island == 1:
    print(total_bridge_len)
else:
    print(-1)