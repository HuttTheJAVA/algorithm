import sys
from collections import deque
input = sys.stdin.readline

six_num = []

n = int(input())

already_done = [0]*(n+1)

num = 1
bias = 5

while(1):
    if num > 1000000:
        break
    six_num.append(num)
    num += bias
    bias += 4

qu = deque()

qu.append((0,0))
already_done[0] = 1
while(1):
    now,cnt = qu.popleft()
    if now == n:
        print(cnt)
        break

    for six_n in six_num:
        if now + six_n <= n:
            if not already_done[now+six_n]:
                qu.append((now+six_n,cnt+1))
                already_done[now+six_n] = 1
        else:
            break