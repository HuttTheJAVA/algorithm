import sys
from collections import deque
input = sys.stdin.readline

INF = (1e9)

n,m,k,x = map(int,input().split())

dp = [INF]*(n)

dp[x-1] = 0

group = [[] for  i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    group[a-1].append(b-1)

def bfs(start):
    qu = deque()
    qu.append(start)
    
    while qu:
        start = qu.popleft()
        for city in group[start]:
            if dp[city]>dp[start]+1:
                dp[city] = dp[start]+1
                qu.append(city)

bfs(x-1)

exsist = False

for i in range(len(dp)):
    if dp[i] == k:
        exsist = True
        print(i+1)

if exsist == False:
    print(-1)