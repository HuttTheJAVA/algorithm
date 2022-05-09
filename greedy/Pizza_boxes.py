from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

delete = []

for i in range(n):
    max_val = -1
    idx = -1
    for j in range(m):
        if matrix[i][j]>max_val:
            max_val=matrix[i][j]
            idx = j
    delete.append((i,idx))
    

for i in range(m):
    max_val = -1
    idx = -1
    for j in range(n):
        if matrix[j][i]>max_val:
            max_val=matrix[j][i]
            idx = j
    delete.append((idx,i))

for x,y in delete:
    matrix[x][y] = 0

hab = 0

for i in range(n):
    hab += sum(matrix[i])

print(hab)