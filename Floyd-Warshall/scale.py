import sys
input = sys.stdin.readline

n = int(input())

INF = sys.maxsize

m = int(input())

matrix = [[INF]*n for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j]>matrix[i][k]+matrix[k][j]:
                if matrix[i][k] == matrix[k][j]:
                    matrix[i][j] = matrix[i][k]
                    matrix[j][i] = abs(matrix[i][k]-1)

for i in range(n):
    matrix[i][i] = 0

for i in range(n):
    print(matrix[i].count(INF))