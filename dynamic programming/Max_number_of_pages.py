import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

chap = [(0,0)]

for i in range(m):
    day,pages = map(int,input().split())
    chap.append((day,pages))

matrix = [[0]*(n+1) for i in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if j>=chap[i][0]:
            matrix[i][j] = max(matrix[i-1][j],matrix[i-1][j-chap[i][0]]+chap[i][1])
        else:
            matrix[i][j] = max(matrix[i-1][j],matrix[i][j])

print(matrix[m][n])