import sys
input = sys.stdin.readline

n = int(input())
num = input().strip()
INF = (1e9)
dp = [INF]*1001

dp[0] = 0

for i in range(n):
    for j in range(i):
        if num[i] == "B":
            if num[j] == 'J':
                dp[i] = min(dp[i],dp[j]+(i-j)**2)
        
        if num[i] == "O":
            if num[j] == 'B':
                dp[i] = min(dp[i],dp[j]+(i-j)**2)

        if num[i] == "J":
            if num[j] == 'O':
                dp[i] = min(dp[i],dp[j]+(i-j)**2)

if dp[n-1] == INF:
    print(-1)
else:
    print(dp[n-1])