from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

day_price = []

for i in range(n):
    day_price.append(int(input()))

coins = 0

for i in range(n-1):
    if day_price[i+1]>day_price[i]:
        coins += m//day_price[i]
        m -= (m//day_price[i])*day_price[i]
    elif day_price[i+1]<day_price[i]:
        if coins:
            m += coins*day_price[i]
            coins = 0

if coins:
    m += day_price[-1]*coins

print(m)