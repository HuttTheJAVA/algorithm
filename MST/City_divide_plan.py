import sys
input = sys.stdin.readline

n,m = map(int,input().split())

road_lst = []

parent = [i for i in range(n+1)]

road_cost = 0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y,cost):
    global road_cost
    global max_cost
    x_p = find(x)
    y_p = find(y)
    if x_p == y_p:
        return
    if x_p<=y_p:
        parent[y_p] = parent[x_p]
    else:
        parent[x_p] = parent[y_p]
    road_cost += cost
    max_cost = max(max_cost,cost)

for i in range(m):
    a,b,c = map(int,input().split())
    road_lst.append((a,b,c))

road_lst.sort(key=lambda x:(x[2],x[0],x[1]))

max_cost = 0

for i in range(len(road_lst)):
    city1,city2,cost = road_lst[i]
    union(city1,city2,cost)

print(road_cost - max_cost)
