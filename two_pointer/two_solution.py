from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

liquid_lst = list(map(int,input().split()))

end = n-1

start = 0

result = []

liquid_lst.sort()

while(end>start):
    hab = liquid_lst[end] + liquid_lst[start]
    result.append((abs(0-hab),liquid_lst[start],liquid_lst[end]))
    if hab == 0:
        break
    elif hab < 0:
        start += 1
    elif hab > 0:
        end -= 1

result.sort()

value,start,end = result.pop(0)

print(start,end)