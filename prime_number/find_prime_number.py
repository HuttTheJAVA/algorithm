import sys
import math

input = sys.stdin.readline

m,n = map(int,input().split())

sosu = []

for num in range(m,n+1):
    result = True
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            result = False
            break
    if result == True:
        sosu.append(num)

for j in sosu:
    if j == 1:
        continue
    print(j)