import sys
from collections import deque

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

d = [0]*(68)

d[0] = 1
d[1] = 1
d[2] = 2
d[3] = 4

def fibo(n):
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1)+fibo(n-2)+fibo(n-3)+fibo(n-4)
    return d[n]

for i in range(n):
    print(fibo(int(input())))