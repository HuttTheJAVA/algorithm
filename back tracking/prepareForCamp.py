import sys
input = sys.stdin.readline

n,l,r,x = map(int,input().split())

problem_lst = list(map(int,input().split()))

problem_lst.sort()

cnt = 0

def backTracking(idx,hab,lst):
    global cnt
    if (l<=hab<=r) and lst[-1]-lst[0]>=x:
        cnt += 1
    for i in range(idx+1,n):
        lst.append(problem_lst[i])
        backTracking(i,hab+problem_lst[i],lst)
        lst.pop()

for i in range(n):
    backTracking(i,problem_lst[i],[problem_lst[i]])

print(cnt)