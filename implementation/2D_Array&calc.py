import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())

A = []

for i in range(3):
    lst = list(map(int,input().split()))
    A.append(lst)

sec = 0

def calc_R_or_C(row_or_col,col_or_row,R_or_C):
    global A
    max_col_or_row = 0
    new_A = []
    for i in range(len(row_or_col)):
        cnt_num = [0]*101
        new_lst = []
        for j in range(len(col_or_row)):
            if R_or_C == 'R':
                if A[i][j]:
                    cnt_num[A[i][j]] += 1
            else:
                if A[j][i]:
                    cnt_num[A[j][i]] += 1
        for j in range(1,len(cnt_num)):
            if cnt_num[j]:
                new_lst.append((j,cnt_num[j]))
        new_lst.sort(key=lambda x:(x[1],x[0]))
        
        new_B = []
        for j in range(len(new_lst)):
            for l in range(len(new_lst[j])):
                new_B.append(new_lst[j][l])
            if len(new_B) > max_col_or_row:
                max_col_or_row = len(new_B)
        new_A.append(new_B)
    return max_col_or_row,new_A

while(sec<=100):
    if 0<=r-1<len(A) and 0<=c-1<len(A[0]):
        if A[r-1][c-1] == k:
            break

    if len(A)>= len(A[0]):
        max_row,new_A = calc_R_or_C(A,A[0],'R')

        for i in range(len(new_A)):
            new_A[i] = new_A[i] + [0]*(max_row - len(new_A[i]))
            if len(new_A[i]) > 100:
                new_A[i] = new_A[i][:100]

        A = new_A
    else:
        max_col,new_A = calc_R_or_C(A[0],A,'C')
        if max_col <= 100:
            new_A2 = [[0]*len(A[0]) for _ in range(max_col)]
        else:
            new_A2 = [[0]*len(A[0]) for _ in range(100)]

        for i in range(len(new_A)):
            for j in range(len(new_A[i])):
                new_A2[j][i] = new_A[i][j]
        
        A = new_A2

    sec += 1

if sec<=100:
    print(sec)
else:
    print(-1)