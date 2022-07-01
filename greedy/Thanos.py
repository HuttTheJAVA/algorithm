from collections import deque
import sys
input = sys.stdin.readline

number = list(map(int,input().strip()))

zeros = number.count(0)
ones = number.count(1)

count = 0

for i in range(len(number)):
    if number[i] == 1 and count<ones//2:
        number[i] = 3
        count += 1

count = 0

for j in range(len(number)-1,-1,-1):
    if number[j] == 0 and count<zeros//2:
        number[j] = 3
        count += 1

for i in range(len(number)):
    if number[i] == 3:
        continue
    else:
        print(number[i],end="")
