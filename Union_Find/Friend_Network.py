import heapq
import sys
import copy

input = sys.stdin.readline

t = int(input())

def find_parent(x): 
    if x == parent_dct[x]:
        return x
    else:
        parent_dct[x] = find_parent(parent_dct[x])
        return parent_dct[x]

def union(x,y):
    global union_cnt
    global parent_dct
    try:
        a = parent_dct[x]
    except:
        parent_dct[x] = x
        union_cnt[x] = 1
    try:
        b = parent_dct[y]
    except:
        parent_dct[y] = y
        union_cnt[y] = 1

    x_p = find_parent(x)
    y_p = find_parent(y)
    if x_p != y_p:
        if union_cnt[x_p]>=union_cnt[y_p]:
            parent_dct[y_p] = parent_dct[x_p]
            union_cnt[x_p] += union_cnt[y_p]
            del union_cnt[y_p]
            return union_cnt[x_p]
        else:
            parent_dct[x_p] = parent_dct[y_p]
            union_cnt[y_p] += union_cnt[x_p]
            del union_cnt[x_p]
            return union_cnt[y_p]
    else:
        return union_cnt[x_p]

for _ in range(t):
    n = int(input())
    parent_dct = {}
    union_cnt = {}

    for i in range(n):
        x,y = input().split()
        print(union(x,y))