import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

n_lst = list(map(int,input().split()))

start_idx = list(map(int,input().split()))

pile_lst = []

for i in range(len(start_idx)):
    if i+1<len(start_idx):
        pile_lst.append((sum(n_lst[start_idx[i]-1:start_idx[i+1]-1]),start_idx[i]))
    else:
        pile_lst.append((sum(n_lst[start_idx[i]-1:]),start_idx[i]))

pile_lst.sort(key=lambda x:(-x[0],x[1]))

ans = [ ]

for i in range(m):
    ans.append(pile_lst[i][1])
ans.sort()
for i in range(len(ans)):
    print(ans[i])