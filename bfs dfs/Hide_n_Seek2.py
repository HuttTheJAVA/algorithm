import sys
from collections import deque
input = sys.stdin.readline

me,brother = map(int,input().split())

dp = [sys.maxsize]*(100001)
cnt = [0]*100001
dp[me] = 0
cnt[me] = 1
qu = deque()
qu.append((me,0))

while(qu):
    now,time = qu.popleft()
    if 100001>now-1>=0:
        if dp[now-1] >= time+1:
            dp[now-1] = time+1
            qu.append((now-1,time+1))
            cnt[now-1] += 1
    if 100001>now+1>=0:
        if dp[now+1] >= time+1:
            dp[now+1] = time+1
            qu.append((now+1,time+1))
            cnt[now+1] += 1
    if 100001>now*2>=0:
        if dp[now*2] >= time+1:
            dp[now*2] = time+1
            qu.append((now*2,time+1))
            cnt[now*2] += 1
print(dp[brother])
print(cnt[brother])