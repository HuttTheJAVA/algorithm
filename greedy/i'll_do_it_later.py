import sys
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    lst.append(tuple(map(int,input().split())))

lst.sort(key=lambda x:(x[1],x[0]))

max_play_day = sys.maxsize

stack_day = 0

for i in lst:
    stack_day += i[0]
    if i[1] - stack_day < max_play_day:
        max_play_day = i[1] - stack_day

print(max_play_day)