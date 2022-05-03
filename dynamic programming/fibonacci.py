import sys
input = sys.stdin.readline

n = int(input())

fibo_ns = []
for i in range(n):
    fibo_ns.append(int(input()))

dp = [0]*45
dp[1] = 1
dp[2] = 1

for i in range(3,45):
    dp[i] = dp[i-1] + dp[i-2]

for num in fibo_ns:
    lst = []
    while(num!=0):
        for j in range(len(dp)-1,0,-1):
            if num>=dp[j]:
                num -= dp[j]
                lst.append(dp[j])
    for vla in lst[::-1]:
        print(vla,end=" ")
    print()