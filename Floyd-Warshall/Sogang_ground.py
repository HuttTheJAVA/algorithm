import sys
input = sys.stdin.readline

INF = sys.maxsize

n,m,r = map(int,input().split())

items = list(map(int,input().split()))

matrix = [[INF]*n for i in range(n)]

for i in range(r):
    a,b,l = map(int,input().split())
    matrix[a-1][b-1] = l
    matrix[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > matrix[i][k]+matrix[k][j]:
                matrix[i][j] = matrix[i][k]+matrix[k][j]

for i in range(n):
    matrix[i][i] = INF

max_val = -1

for i in range(n):
    hab = items[i]
    for j in range(n):
        if matrix[i][j] <= m:
            hab += items[j]
    max_val = max(max_val,hab)

print(max_val)