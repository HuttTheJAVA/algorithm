import sys
input = sys.stdin.readline

n = int(input())

n_lst = []

for i in range(n):
    a,b = map(int,input().split())
    n_lst.append((a,b))

n_lst.sort(key=lambda x:-x[1])

start = n_lst.pop()[1]

n_lst.sort(key=lambda x:x[0])

end = n_lst.pop()[0]

if end<=start:
    print(0)
else:
    print(end-start)