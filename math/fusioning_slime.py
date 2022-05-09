import sys
input = sys.stdin.readline


n = int(input())

n_lst = list(map(int,input().split()))
n_lst.sort(reverse=True)
score = 0
while(len(n_lst)!=1):
    a = n_lst.pop()
    b = n_lst.pop()
    score += a*b
    n_lst.append(a+b)

print(score)