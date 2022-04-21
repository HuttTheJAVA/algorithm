import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())

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

for i in range(n):
    matrix[i][i] = 'me!'

cnt = 0

for i in range(n):
    INFs = matrix[i].count(INF)
    bigs = matrix[i].count(1)
    smalls = matrix[i].count(0)
    half = n//2
    if INFs>=half or bigs<=half and smalls<=half:
        continue
    else:
        cnt += 1

print(cnt)