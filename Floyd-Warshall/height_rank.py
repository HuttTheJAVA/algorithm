import sys
input = sys.stdin.readline

n,m = map(int,input().split())

INF = sys.maxsize

matrix = [['?']*n for i in range(n)]

for i in range(n):
    matrix[i][i] = 'myself'

for i in range(m):
    a,b = map(int,input().split())
    matrix[a-1][b-1] = 's'
    matrix[b-1][a-1] = 't'

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][k] == matrix[k][j] and matrix[i][k] != '?':
                matrix[i][j] = matrix[i][k]
    
cnt = 0

for i in range(n):
    if matrix[i].count('?'):
        continue
    else:
        cnt += 1

print(cnt)