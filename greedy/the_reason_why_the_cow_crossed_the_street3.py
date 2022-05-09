from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

imigration = []

for i in range(n):
    a,b = map(int,input().split())
    imigration.append((a,b))

imigration.sort(key=lambda x:(x[0],x[1]))

time = imigration[0][0] + imigration[0][1]

for i in range(1,n):
    if imigration[i][0]>=time:
        time = imigration[i][0]+imigration[i][1]
    else:
        time += imigration[i][1]

print(time)