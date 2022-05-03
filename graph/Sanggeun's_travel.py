import sys

input = sys.stdin.readline

T = int(input())




def find_parent(num):
    if num != parent[num]:
        parent[num] = find_parent(parent[num])
    return parent[num]

def union(num1,num2):
    num1 = find_parent(num1)
    num2 = find_parent(num2)
    if num1<num2:
        parent[num2] = num1
    else:
        parent[num1] = num2

for _ in range(T):
    flight = 0
    N,M = map(int,input().split())
    parent = [i for i in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        if find_parent(a) != find_parent(b):
            union(a,b)
            flight += 1

    print(flight)