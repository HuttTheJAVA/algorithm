import sys
import copy
input = sys.stdin.readline

n = int(input())

A = [0]*101
B = [0]*101
to_make = 0
for i in range(n):
    a,b = map(int,input().split())
    A[a] += 1
    B[b] += 1
    tmp_A = copy.deepcopy(A)
    tmp_B = copy.deepcopy(B)
    pointer_A = 1
    pointer_B = 100
    to_make += 2
    done_make = 0
    max_val = 0
    while(done_make<to_make):
        while(not A[pointer_A]):
            pointer_A += 1
        while(not B[pointer_B]):
            pointer_B -= 1
        minus = min(A[pointer_A],B[pointer_B])
        A[pointer_A] -= minus
        B[pointer_B] -= minus
        max_val = max(max_val,pointer_A+pointer_B)
        done_make += 2*minus
    A = copy.deepcopy(tmp_A)
    B = copy.deepcopy(tmp_B)
    
    print(max_val)


