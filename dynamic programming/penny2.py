import sys
input = sys.stdin.readline


n,k = map(int,input().split())

INF = (1e9)

d = [INF]*(10001)

d[0] = 0

coin_lst = []

for i in range(n):
    coin_lst.append(int(input()))
for i in range(1,k+1):
    for j in coin_lst:
        if i-j>=0:
            d[i] = min(d[i-j]+1,d[i])

if d[k] != INF:
    print(d[k])
else:
    print(-1)