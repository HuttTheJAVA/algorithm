import sys
input = sys.stdin.readline

n,m = map(int,input().split())

node = [i for i in range(n)]

def find(x):
    if node[x] == x:
        return x
    return find(node[x])

def union(x,y):
    global node
    p_x = find(x)
    p_y = find(y)
    if p_x == p_y:
        return "Cycle"
    if p_x<=p_y:
        node[p_y] = p_x
    else:
        node[p_x] = p_y
    return "not yet"
res = -1
for i in range(m):
    x,y = map(int,input().split())
    if res != -1:
        continue
    if union(x,y) == "Cycle" and res == -1:
        res = i+1

if res>=0:
    print(res)
else:
    print(0)