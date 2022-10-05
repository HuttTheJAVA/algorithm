import heapq
import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())

parent = [i for i in range(n+1)]

def find(x):
    global parent
    if x == parent[x]:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x,y): # y그룹을 x그룹에 속하게 함.
    global parent
    x_parent = find(x)
    y_parent = find(y)
    parent[x_parent] = y_parent

for i in range(m):
    calc,x,y = map(int,input().split())
    if calc:
        x_parent = find(x)
        y_parent = find(y)
        if x_parent == y_parent:
            print("YES")
        else:
            print("NO")
    else:
        union(x,y)