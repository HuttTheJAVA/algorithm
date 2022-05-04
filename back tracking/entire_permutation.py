import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

n_lst = [i for i in range(1,n+1)]

per = permutations(n_lst)

for i in per:
    for j in i:
        print(j,end=" ")
    print()
