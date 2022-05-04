import sys
input = sys.stdin.readline

n = int(input())



card = list(map(int,input().split()))

card = [0]+card

dp = [0]*(n+1)

for i in range(1,n+1):
    dp[i] = card[i]


def max_money():
    for i in range(2,len(card)):
        for j in range(1,i):
            dp[i] = max(dp[i],dp[i-j]+card[i-(i-j)])

max_money()

print(dp[n])