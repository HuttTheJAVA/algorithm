import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

max_score = -1

def bruteForce(lst,score):
    global max_score
    if len(lst) <= 2:
        max_score = max(max_score,score)
        return
    for i in range(1,len(lst)-1):
        bruteForce(lst[:i]+lst[i+1:],score+lst[i-1]*lst[i+1])

bruteForce(n_lst,0)
print(max_score)