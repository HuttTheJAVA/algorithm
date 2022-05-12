import sys

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    lst = list(input().strip())
    matrix.append(list(map(int,lst)))

max_square_num = -1

def make_square_num(before_x,before_y,seq_x,seq_y,number):
    global max_square_num
    global n
    global m


    if int(int(number)**0.5) == int(number)**0.5:
        max_square_num = max(max_square_num,int(number))
    if int(int(number[::-1])**0.5) == int(number[::-1])**0.5:
        max_square_num = max(max_square_num,int(number[::-1]))
    
    if seq_x == None and seq_y == None:
        for i in range(-len(matrix),len(matrix)):
            for j in range(-len(matrix),len(matrix[0])):
                if not(before_x + i == before_x and before_y + j == before_y) and 0<=before_x + i<n and 0<=before_y + j<m:
                    new_number = number + str(matrix[before_x + i][before_y + j])
                    make_square_num(before_x + i,before_y + j,i,j,new_number)
    else:
        i = before_x + seq_x
        j = before_y + seq_y
        if 0<=i<n and 0<=j<m:
            make_square_num(i,j,seq_x,seq_y,number+str(matrix[i][j]))

for i in range(n):
    for j in range(m):
        make_square_num(i,j,None,None,str(matrix[i][j]))

print(max_square_num)