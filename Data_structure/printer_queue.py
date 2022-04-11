from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    n,m = map(int,input().split())
    printer = deque(list(map(int,input().split())))
    idx = m
    rank = 1
    while(1):
        if printer[0] == max(printer):
            if idx == 0:
                print(rank)
                break
            else:
                printer.popleft()
                idx -= 1
                rank += 1
        else:
            if idx == 0:
                idx = len(printer)-1
                printer.append(printer.popleft())
            else:
                idx -= 1
                printer.append(printer.popleft())