import sys
input = sys.stdin.readline

n,m = map(int,input().split())

res = []

for i in range(n):
    p,l = map(int,input().split())
    lst = list(map(int,input().split()))
    if p<l:
        res.append(1)
    else:
        lst.sort()
        lst = lst[-l:]
        res.append(lst[0])

res.sort()

clasS = 0

for i in range(len(res)):
    if m>=res[i]:
        m -= res[i]
        clasS += 1
    else:
        break

print(clasS)