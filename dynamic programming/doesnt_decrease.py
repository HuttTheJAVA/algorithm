import sys
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    leng = int(input())
    lst.append(leng)

dp = [[] for i in range(65)]
for i in range(10):
    dp[1].append(1)

for i in range(2,max(lst)+1):
    dp[i].append(sum(dp[i-1]))
    for j in range(9):
        dp[i].append(dp[i][-1]-dp[i-1][j])

for i in lst:
    print(sum(dp[i]))