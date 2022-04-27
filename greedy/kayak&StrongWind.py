import sys
input = sys.stdin.readline

n,s,r = map(int,input().split())

broke = list(map(int,input().split()))

spare = list(map(int,input().split()))

dp = [1]*(n+1)

for i in broke:
    dp[i] -= 1

for j in spare:
    dp[j] += 1

for i in range(n+1):
    if dp[i]>1:
        if i-1>=0 and dp[i-1] == 0:
            dp[i] -= 1
            dp[i-1] += 1
        elif i+1 <= n and dp[i+1] == 0:
            dp[i] -= 1
            dp[i+1] += 1
    
print(dp.count(0))
