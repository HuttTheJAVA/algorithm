import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

n_lst = []

for i in range(n):
    n_lst.append(int(input()))

print(round(sum(n_lst)/len(n_lst)))
n_lst.sort()
print(n_lst[len(n_lst)//2])
c = Counter(n_lst)
lst = c.most_common()
if len(lst)>=2:
    if lst[0][1] == lst[1][1]:
        print(lst[1][0])
    else:
        print(lst[0][0])
else:
    print(lst[0][0])

print(n_lst[-1]-n_lst[0])