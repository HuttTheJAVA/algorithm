import sys

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

arr = []

max_arr = 0

def find_max(idx):
    global max_arr
    arr.append(n_lst[idx])
    if len(arr)==n:
        hab = 0
        for i in range(n-1):
            hab += abs(arr[i]-arr[i+1])
        max_arr = max(max_arr,hab)
    temp = n_lst[idx]
    del n_lst[idx]
    for i in range(len(n_lst)):
        find_max(i)
    n_lst.insert(idx,temp)
    arr.pop()

for i in range(len(n_lst)):
    find_max(i)

print(max_arr)