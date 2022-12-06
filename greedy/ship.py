import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

crain_lst = list(map(int,input().split()))

m = int(input())

box_lst = list(map(int,input().split()))

crain_lst.sort(reverse=True)
box_lst.sort(reverse=True)

ki_index_val_loadMax = {}

available = [0]*len(crain_lst)

cnt = 0
impossible = False
if box_lst[0] > crain_lst[0]:
    impossible = True
    cnt = -1

if not impossible:
    for i in range(len(box_lst)):
        loaded = False
        for j in range(len(crain_lst)):
            if box_lst[i] <= crain_lst[j]:
                if available[j]:
                    available[j] -= 1
                    loaded = True
                    break
            else:
                cnt += 1
                loaded = True
                for k in range(1,len(crain_lst)):
                    available[k] += 1
                break
        if not loaded:
            cnt += 1
            for k in range(1,len(crain_lst)):
                available[k] += 1

print(cnt)