from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append((a,b))
lst.sort(key=lambda x:(x[0],x[1]))

stack = deque()
loc_stack = deque()
left = 0
right = 0
location = None

for i in range(n):
    stack.append(lst[i][1])
    right += lst[i][1]
    loc_stack.append(lst[i][0])
    if left<right:
        while(left<right):
            val = stack.popleft()
            right -= val
            left += val
            location = loc_stack.popleft()

print(location)