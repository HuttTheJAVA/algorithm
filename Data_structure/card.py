import sys
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

dct = {}

max_num = 0

max_idx = -1

lst.sort()

for i in lst:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1
    if dct[i]>max_num:
        max_num = max(dct[i],max_num)
        max_idx = i
        

print(max_idx)