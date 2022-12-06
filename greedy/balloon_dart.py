from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

height_dct = {}

for i in range(len(lst)):
    try:
        a = height_dct[lst[i]+1]
        height_dct[lst[i]+1] -= 1
        if not height_dct[lst[i]+1]:
            del height_dct[lst[i]+1]
    except:
        pass
    try:
        height_dct[lst[i]] += 1
    except:
        height_dct[lst[i]] = 1

dart = 0

for ki in height_dct.keys():
    dart += height_dct[ki]

print(dart)