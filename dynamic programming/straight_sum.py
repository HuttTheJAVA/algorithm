import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

original_dp = [0]*len(lst)
chance_dp = [0]*len(lst)

original_dp[0] = lst[0]
chance_dp[0] =lst[0]

for i in range(1,len(lst)):
    chance_dp[i] = max(lst[i],chance_dp[i-1]+lst[i],original_dp[i-1],original_dp[i-1]+lst[i])
    original_dp[i] = max(lst[i],original_dp[i-1]+lst[i])

max_val = -sys.maxsize

for i in range(len(lst)):
    max_val = max(max_val,original_dp[i])
    max_val = max(max_val,chance_dp[i])

print(max_val)