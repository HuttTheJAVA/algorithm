import sys

input = sys.stdin.readline

d = [0]*101

n = int(input())

d[1] = 1
d[2] = 1
d[3] = 1

for i in range(4,101):
    d[i] = d[i-2] + d[i-3]

for i in range(n):
    num = int(input())
    print(d[num])