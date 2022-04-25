import sys
input = sys.stdin.readline

n = int(input())

INF = sys.maxsize

matrix = [[INF]*n for i in range(n)]

while(1):
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > matrix[i][k]+matrix[k][j]:
                matrix[i][j] = matrix[i][k]+matrix[k][j]

for i in range(n):
    matrix[i][i] = 0

min_val = INF
cnt = 0
candidate = []

for i in range(n):
    if max(matrix[i]) < min_val:
        min_val = max(matrix[i])
        cnt = 1
        candidate = [i+1]
    elif max(matrix[i]) == min_val:
        cnt += 1
        candidate.append(i+1)

print(min_val,cnt)
for i in candidate:
    print(i,end=" ")
