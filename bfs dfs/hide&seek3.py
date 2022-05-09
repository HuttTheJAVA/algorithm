from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())

time_idx = [0]*(100001)
visited = [False]*(100001)



def bfs(n):
    qu = deque()
    qu.append(n)
    visited[n] = True
    while(qu):
        me = qu.popleft()

        if me == k:
            print(time_idx[k])
            return
        if me*2<=len(visited)-1:
            if visited[me*2]==False:
                visited[me*2] = True
                qu.append(me*2)
                time_idx[me*2] = time_idx[me]

        if me-1>=0 and me <= len(visited)-1:
            if visited[me-1]==False:
                visited[me-1] = True
                qu.append(me-1)
                time_idx[me-1] = time_idx[me]+1

        if me+1>0 and me+1<=len(visited)-1:
            if visited[me+1] == False:
                visited[me+1] = True
                qu.append(me+1)
                time_idx[me+1] = time_idx[me]+1


bfs(n)