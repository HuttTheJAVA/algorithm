import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    a = list(map(int,input().split()))
    lst.append(a)

for i in range(1,n):
    for j in range(len(lst[i])):
        if j != 0 and j!=len(lst[i])-1:
            lst[i][j] = max(lst[i-1][j-1],lst[i-1][j])+lst[i][j]
        elif j==0:
            lst[i][j] = lst[i][j]+lst[i-1][j]
        elif j == len(lst[i])-1:
            lst[i][j] = lst[i][j]+lst[i-1][j-1]
            
print(max(lst[n-1]))