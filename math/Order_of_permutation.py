from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

order_lst = list(map(int,input().split()))

num_lst = [i for i in range(1,n+1)]

is_one = order_lst[0]
order_lst = order_lst[1:]

def factorial(num):
    res= 1
    while(num>0):
        res *= num
        num -= 1
    return res

if is_one == 1:
    rank_permutation = []
    rank = order_lst[0] - 1
    while(num_lst):
        for i in range(len(num_lst)-1,-1,-1):
            number_of_cases = len(num_lst[:i])*factorial(n-1 - len(rank_permutation))
            if rank >= number_of_cases:
                rank_permutation.append(num_lst.pop(i))
                rank -= number_of_cases
                break
    print(*rank_permutation)

else:
    rank = 1
    for i in range(len(order_lst)):
        idx = num_lst.index(order_lst[i])
        num_lst.pop(idx)
        rank += idx*factorial(len(num_lst))
    print(rank)