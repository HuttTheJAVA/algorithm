import sys

input = sys.stdin.readline

n,square_time = map(int,input().split())

matrix = []

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

matrix_dp_dct = {}

matrix_dp_dct[1] = matrix

def times_matrix(matrix1,matrix2):
    global n
    new_matrix = [[0]*n for i in range(n)] # 같은 크기 곱하기 때문에 크기변화 x 라 n으로 설정가능.
    for i in range(n):
        for j in range(n):
            hab = 0
            for k in range(n):
                hab += (matrix1[i][k]*matrix2[k][j])%1000
            new_matrix[i][j] = hab
    return new_matrix

def square_matrix(num):
    global n
    global matrix_dp_dct
    try:
        a = matrix_dp_dct[num]
        return matrix_dp_dct[num]
    except:
        if num%2:
            matrix1 = square_matrix(num//2)
            matrix2 = square_matrix(num-num//2)
            new_matrix = times_matrix(matrix1,matrix2)
            matrix_dp_dct[num] = new_matrix
        else:
            matrix1 = square_matrix(num//2)
            new_matrix = times_matrix(matrix1,matrix1)
            matrix_dp_dct[num] = new_matrix
        return matrix_dp_dct[num]

res_matrix = square_matrix(square_time)

for i in range(n):
    for j in range(n):
        print(res_matrix[i][j]%1000,end=" ")
    print()