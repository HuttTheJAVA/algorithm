import sys

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

n_lst.sort()

x = int(input())

count = 0

start = 0
end = len(n_lst)-1

while(end>start):
    if n_lst[start]+n_lst[end] == x:
        count += 1
        end -= 1
        start += 1
    elif n_lst[start]+n_lst[end] < x:
        start += 1
    elif n_lst[start]+n_lst[end] > x:
        end -= 1

print(count)