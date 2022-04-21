from collections import deque
import sys

input = sys.stdin.readline

com = int(input())
n = int(input())


visited = [False]*(com+1)

n_lst = [[]for i in range(com+1)]

for i in range(n):
    a,b = map(int,input().split())
    n_lst[a].append(b)
    n_lst[b].append(a)

result = set()

def BFS(n):
    qu = deque()
    qu.append(n)
    while(qu):
        val = qu.popleft()
        result.add(val)
        if visited[val] == False:
            visited[val] = True
            qu.extend(n_lst[val])

BFS(1)

print(len(result)-1)