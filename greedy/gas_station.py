import sys
input = sys.stdin.readline
n = int(input())

km = list(map(int,input().split()))

price = list(map(int,input().split()))

spend = km[0]*price[0]
location = km[0]

min_idx = 0

for i in range(1,len(price)-1):
    if price[i]>price[min_idx]:
        spend += km[i]*price[min_idx]
    else:
        min_idx = i
        spend += km[i]*price[min_idx]

print(spend)