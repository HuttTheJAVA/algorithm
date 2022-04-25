import sys
input = sys.stdin.readline

n = int(input())

n_lst = []
for i in range(n):
    n_lst.append(int(input()))

pivot = n_lst[-1]

cnt = 0

for i in range(n-2,-1,-1):
    if n_lst[i]>=pivot:
        cnt += n_lst[i]-pivot+1
        pivot = n_lst[i]-(n_lst[i]-pivot+1)
    else:
        pivot = n_lst[i]

print(cnt)