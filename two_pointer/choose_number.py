import sys

n,m = map(int,input().split())

lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

point1 = 0
point2 = 0

gap = sys.maxsize

while(1):
    if lst[point2] - lst[point1] == m:
        gap = m
        break
    elif lst[point2] - lst[point1] > m:
        gap = min(gap,lst[point2]-lst[point1])
        point1 += 1
    else:
        point2 += 1
        if point2 == len(lst):
            break

print(gap)