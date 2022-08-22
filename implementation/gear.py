from collections import deque
import sys
input = sys.stdin.readline

gears = []

for i in range(4):
    gear = list(map(int,list(input().strip())))
    gears.append(gear)

move = int(input())

move_command = []

for i in range(move):
    gear_num,clock_wise = map(int,input().split())
    move_command.append((gear_num-1,clock_wise))

qu = deque()

for cmd in move_command:
    qu.append((cmd[0],cmd[1]))
    visit = [0]*4
    visit[cmd[0]] = 1
    while(qu):
        gear_n,clock_wise = qu.popleft()
        if gear_n-1>=0 and not visit[gear_n-1] and (gears[gear_n-1][2] != gears[gear_n][6]):
            qu.append((gear_n-1,clock_wise*-1))
            visit[gear_n-1] = 1
        if gear_n+1<4 and not visit[gear_n+1] and (gears[gear_n+1][6] != gears[gear_n][2]):
            qu.append((gear_n+1,clock_wise*-1))
            visit[gear_n+1] = 1
        if clock_wise == 1:
            gears[gear_n] = [gears[gear_n][-1]]+gears[gear_n][:-1]
        else:
            gears[gear_n] = gears[gear_n][1:]+[gears[gear_n][0]]

score = 0
if gears[0][0]:
    score += 1
if gears[1][0]:
    score += 2
if gears[2][0]:
    score += 4
if gears[3][0]:
    score += 8

print(score)