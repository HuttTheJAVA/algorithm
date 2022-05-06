import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if n_lst[j]>n_lst[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))