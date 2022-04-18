import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coin_lst = [0]

for i in range(n):
    coin_lst.append(int(input()))

coin_lst.sort()

matrix1 = [0]*(k+1)
matrix2 = [0]*(k+1)
matrix1[0] = 1
matrix2[0] = 1

for i in range(1,len(coin_lst)):
    for j in range(1,k+1):
        matrix2[j] += matrix1[j]
        if j - coin_lst[i]>=0:
            matrix2[j] += matrix2[j-coin_lst[i]]
    matrix1 = matrix2
    matrix2 = [0]*(k+1)
    matrix2[0] = 1

print(matrix1[-1])