a = int(input())

n_lst = list(map(int,input().split()))

dp = [0]*len(n_lst)

for i in range(1,len(n_lst)):
    for j in range(i):
        if n_lst[i]>n_lst[j]:
            dp[i] = max(dp[j]+1,dp[i])

pivot = max(dp)
print(pivot+1)
result = []
for i in range(len(dp)-1,-1,-1):
    if dp[i] == pivot:
        result.append(n_lst[i])
        pivot -= 1

for i in result[::-1]:
    print(i,end=" ")