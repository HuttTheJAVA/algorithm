from collections import deque
from itertools import product
import sys
import copy
input = sys.stdin.readline

n,k,p,x = map(int,input().split())

num_change_time_matrix = [[0,4,3,3,4,3,2,3,1,2],
                          [4,0,5,3,2,5,6,1,5,4],
                          [3,5,0,2,5,4,3,4,2,3],
                          [3,3,2,0,3,2,3,2,2,1],
                          [4,2,5,3,0,3,4,3,3,2],
                          [3,5,4,2,3,0,1,4,2,1],
                          [2,6,3,3,4,1,0,5,1,2],
                          [3,1,4,2,3,4,5,0,4,3],
                          [1,5,2,2,3,2,1,4,0,1],
                          [2,4,3,1,2,1,2,3,1,0]]

numbers = ['0','1','2','3','4','5','6','7','8','9']

cnt = 0

str_x = '0'*(k-len(str(x)))+str(x)

for i in product(numbers,repeat=k):
    now_num = ''
    tmp_p = p
    for num in i:
        now_num += num
    if int(now_num) > n:
        break
    
    res = True

    for idx in range(len(now_num)):
        if tmp_p >= num_change_time_matrix[int(str_x[idx])][int(now_num[idx])]:
            tmp_p -= num_change_time_matrix[int(str_x[idx])][int(now_num[idx])]
        else:
            res = False
            break
    
    if res and tmp_p != p and int(now_num)>0:
        cnt += 1

print(cnt)
