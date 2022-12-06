import sys

input = sys.stdin.readline

n,x = map(int,input().split())

lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append((a,b,abs(a-b)))

lst.sort(key=lambda x:(-x[2],x[1],x[0]))

taste = 0

for i in range(len(lst)):
    if lst[i][0] > lst[i][1] and x >= 5000 + 1000*(len(lst)-i-1):
        taste += lst[i][0]
        x -= 5000
    else:
        taste += lst[i][1]
        x-= 1000

print(taste)