import sys
input = sys.stdin.readline

n = int(input())

m = int(input())

city = [i for i in range(n+1)]

def find(x):
    if city[x] == x:
        return x
    return find(city[x])

def union(x,y):
    global city
    p_x = find(x)
    p_y = find(y)
    if p_x<=p_y:
        city[p_y] = p_x
    else:
        city[p_x] = p_y

for i in range(1,n+1):
    lst = list(map(int,input().split()))
    for j in range(len(lst)):
        if lst[j]:
            union(i,j+1)

plan_order = list(map(int,input().split()))

can = True

for i in range(1,len(plan_order)):
    if find(plan_order[i-1]) != find(plan_order[i]):
        can = False
        break
if can:
    print("YES")
else:
    print("NO")