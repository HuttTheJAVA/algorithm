import sys
import math as m
input = sys.stdin.readline

n = int(input())

my_list = list(map(int,input().split()))

wish_list = list(map(int,input().split()))

dct = {}

for i in range(n):
    if my_list[i] in dct:
        dct[my_list[i]] += 1
    else:
        dct[my_list[i]] = 1

match = 0

for i in range(n):
    if wish_list[i] not in dct:
        continue
    elif dct[wish_list[i]] == 0:
        continue
    else:
        dct[wish_list[i]] -= 1
        match += 1

print(n-match)