import sys

input = sys.stdin.readline

n = int(input())

k = int(input())

sensor_lst = list(map(int,input().split()))

sensor_lst.sort()

dist_gap = []

for i in range(1,len(sensor_lst)):
    dist_gap.append(abs(sensor_lst[i]-sensor_lst[i-1]))

dist_gap.sort()

for i in range(k-1):
    if dist_gap:
        dist_gap.pop()
    else:
        break


print(sum(dist_gap))
