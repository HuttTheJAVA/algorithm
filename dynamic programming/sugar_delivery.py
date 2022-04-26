import sys

input = sys.stdin.readline

INF = (1e9)

n = int(input())

d = [INF]*5001

d[3] = 1
d[5] = 1

for i in range(n+1):
    if i-3>=0:
        d[i] = min(d[i],d[i-3]+1)
    if i-5>=0:
        d[i] = min(d[i],d[i-5]+1)

if d[n]>=INF:
    print(-1)
else:
    print(d[n])