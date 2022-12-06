from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

minus_lst = []
zero_cnt = 0
plus_lst = []

for i in range(n):
    if lst[i]<0:
        minus_lst.append(lst[i])
    elif lst[i] == 0:
        zero_cnt += 1
    else:
        plus_lst.append(lst[i])

minus_lst.sort(reverse=True)

plus_lst.sort()

hab =0

while(plus_lst):
    num = plus_lst.pop()
    if plus_lst:
        if num * plus_lst[-1] > num + plus_lst[-1]:
            num *= plus_lst[-1]
            plus_lst.pop()
    hab += num

while(minus_lst):
    num = minus_lst.pop()
    if minus_lst:
        num *= minus_lst[-1]
        minus_lst.pop()
    else:
        if zero_cnt:
            zero_cnt -= 1
            num *= 0
    hab += num

print(hab)