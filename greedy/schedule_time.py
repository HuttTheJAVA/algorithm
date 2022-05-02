import sys
input = sys.stdin.readline

n = int(input())

to_do = []

for i in range(n):
    s,e = map(int,input().split())
    to_do.append((s,e))

to_do.sort(key=lambda x:(x[1],x[0]))

wake_up = sys.maxsize

sum_worked = 0
res = True
for i in range(len(to_do)):
    sum_worked += to_do[i][0]
    if to_do[i][1]-sum_worked >= 0:
        wake_up = min(wake_up,to_do[i][1]-sum_worked)
    else:
        res = False
        break

if res:
    print(wake_up)
else:
    print(-1)