import sys
input = sys.stdin.readline

n,m = map(int,input().split())

INF = sys.maxsize

matrix = [[INF]*n for i in range(n)]

for i in range(n):
    matrix[i][i] = 0

for i in range(m):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>matrix[i][k]+matrix[k][j]:
                matrix[i][j] = matrix[i][k]+matrix[k][j]
    
result = False

for i in range(n):
    if max(matrix[i])>6:
        result = True
        print("Big World!")
        break

if not result:
    print("Small World!")