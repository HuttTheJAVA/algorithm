import sys
input = sys.stdin.readline

n,m = map(int,input().split())

pop = [i+1 for i in range(n)]

dp = [0]*n

relate = []

for i in range(n):
    dp[i] += i

for i in range(len(dp)-1,-1,-1):
    if dp[i]<=m:
        val = pop.pop(i)
        relate.append(val)
        m -= dp[i]

new = relate+pop

for i in new:
    print(i,end=" ")