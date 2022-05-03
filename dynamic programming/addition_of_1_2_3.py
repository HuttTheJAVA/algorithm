import sys
input = sys.stdin.readline

INF = (1e9)

n = int(input())

n_lst = []

for i in range(n):
    n_lst.append(int(input()))

d = [0]*(12)
d[1] = 1
d[2] = 2
d[3] = 4

n_max = max(n_lst)

for i in range(4,n_max+1):
    d[i] = d[i-1]+d[i-2]+d[i-3]


for i in n_lst:
    print(d[i])
