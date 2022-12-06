import sys
input = sys.stdin.readline

n,m = map(int,input().split())

min_dist = [[sys.maxsize]*(n+1) for i in range(n+1)]

start_path = [[None]*(n+1) for i in range(n+1)]

for i in range(1,n+1):
    min_dist[i][i] = sys.maxsize
    start_path[i][i] = '-'

for i in range(m):
    x,y,cost = map(int,input().split())
    min_dist[x][y] = cost
    min_dist[y][x] = cost
    start_path[x][y] = y
    start_path[y][x] = x

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if min_dist[j][i] != '-' and min_dist[i][k] != '-' and j != k:
                if min_dist[j][i] + min_dist[i][k] < min_dist[j][k]:
                    min_dist[j][k] = min_dist[j][i] + min_dist[i][k]
                    start_path[j][k] = start_path[j][i]

for i in range(1,n+1):
    for j in range(1,n+1):
        print(start_path[i][j],end=" ")
    print()