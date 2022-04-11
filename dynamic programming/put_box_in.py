import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

data = [1]*(n)

for i in range(n):
    for j in range(i):
        if n_lst[j]<n_lst[i]:
            data[i] = max(data[i],data[j]+1)

print(max(data))