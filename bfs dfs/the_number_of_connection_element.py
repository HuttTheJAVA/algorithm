import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())
group = [[]for i in range(n+1)]

visit = [0]*(n+1)

def dfs(num):
    visit[num] = 1
    for val in group[num]:
        if visit[val] == 0:
            dfs(val)

for i in range(m):
    u,v = map(int,input().split())

    group[u].append(v)
    group[v].append(u)

count = 0

for i in range(1,n+1):
    if visit[i] != 1:
        dfs(i)
        count += 1

print(count)