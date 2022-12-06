import sys
from collections import deque
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]
round1 = 1
while(1):
    n = int(input())
    matrix = []
    dp = [[sys.maxsize]*n for i in range(n)]
    if not n:
        break
    for i in range(n):
        lst = list(map(int,input().split()))
        matrix.append(lst)
    dp[0][0] = matrix[0][0]
    qu = deque()
    qu.append((0,0))
    while(qu):
        x,y = qu.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<n and 0<=ny<n and dp[nx][ny] > dp[x][y] + matrix[nx][ny]:
                dp[nx][ny] = dp[x][y] + matrix[nx][ny]
                qu.append((nx,ny))
    print(f"Problem {round1}: {dp[-1][-1]}")
    round1 += 1