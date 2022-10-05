import sys

input = sys.stdin.readline

computer = int(input())

edge = int(input())

edge_info = []

record_parent = [i for i in range(computer+1)]

cost = 0

def find(x):
    if record_parent[x] == x:
        return x
    else:
        record_parent[x] = find(record_parent[x])
        return record_parent[x]

def union(x,y,c):
    global cost
    x_p = find(x)
    y_p = find(y)
    if x_p == y_p:
        return
    if x_p <=y_p:
        record_parent[y_p] = x_p
    else:
        record_parent[x_p] = y_p
    cost += c
for i in range(edge):
    a,b,c = map(int,input().split())
    edge_info.append((a,b,c))

edge_info.sort(key=lambda x:(x[2],x[0],x[1]))

for i in range(edge):
    a,b,c = edge_info[i]
    union(a,b,c)

print(cost)