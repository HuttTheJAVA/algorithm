import sys
import math as m
input = sys.stdin.readline

dp = [0]*(1000001)
dp[3] = 1
for i in range(3,len(dp),2):
    cant = False
    if dp[i] == -1:
        continue

    for j in range(3,int(m.sqrt(i))+1):
        if not i%j:
            cant = True
            break
    if cant:
        break
    else:
        dp[i] = 1
    idx = i
    while(1):
        idx += i*2
        if idx>1000000:
            break
        dp[idx] = -1
while(1):

    n = int(input())

    if not n:
        break

    for i in range(n-3,2,-1):
        if dp[i] == 1:
            if dp[n-i] == 1:
                print(f'{n} = {n-i} + {i}')
                break
