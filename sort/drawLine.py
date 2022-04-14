import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lines = []

for i in range(n):
    a,b = map(int,input().split())
    lines.append((a,b))

lines.sort(key=lambda x:(x[0],-x[1]))

min_boundary = lines[0][0]
max_boundary = lines[0][1]

recent_min = None
recent_max = None

cm = 0

for i in range(1,n):
    if lines[i][0]<=max_boundary and lines[i][1]>max_boundary:
        max_boundary = lines[i][1]
    elif lines[i][0]>max_boundary:
        cm += max_boundary-min_boundary
        min_boundary = lines[i][0]
        max_boundary = lines[i][1]  

if recent_min == None and recent_max == None:
    cm += max_boundary-min_boundary
elif recent_min != min_boundary and recent_max != max_boundary:
    cm += max_boundary-min_boundary

print(cm)