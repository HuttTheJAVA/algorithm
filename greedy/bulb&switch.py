import sys
input = sys.stdin.readline
import copy
n = int(input())

now = list(input().strip())

goal = list(input().strip())

tmp = copy.deepcopy(now)
min_cnt = sys.maxsize
def change(i):
    global now
    if now[i] == '0':
        now[i] = '1'
    else:
        now[i] = '0'

def click(i):
    global now
    if i-1>=0:
        change(i-1)
    change(i)
    if i+1 < len(now):
        change(i+1)

cnt = 0
click(0)
cnt += 1
for i in range(1,len(now)):
    if now[i-1] != goal[i-1]:
        click(i)
        cnt += 1

if now == goal:
    min_cnt = min(min_cnt,cnt)

now = copy.deepcopy(tmp)
cnt = 0
for i in range(1,len(now)):
    if now[i-1] != goal[i-1]:
        click(i)
        cnt += 1

if now == goal:
    min_cnt = min(min_cnt,cnt)

if min_cnt != sys.maxsize:
    print(min_cnt)
else:
    print(-1)