import sys
input = sys.stdin.readline

n = int(input().strip())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if not matrix[j][k]:
                if matrix[j][i] and matrix[i][k]:
                    matrix[j][k] = 1

for line in matrix:
    print(*line)