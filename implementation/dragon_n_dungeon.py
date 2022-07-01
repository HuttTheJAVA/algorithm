import sys
from collections import deque
input = sys.stdin.readline

at_least_hp = 0

Stress = 0

N,ATK = map(int,input().split())

rooms = []

for i in range(N):
    info = list(map(int,input().split()))
    rooms.append(info)

for room in rooms:
    if room[0] == 1:
        if room[2]>=ATK and not room[2]%ATK:
            Damage = (room[2]//ATK-1)*room[1]
        else:
            Damage = (room[2]//ATK)*room[1]
        Stress += Damage
        if Stress > at_least_hp:
            at_least_hp = Stress
    else:
        ATK += room[1]
        if room[2]>=Stress:
            Stress = 0
        else:
            Stress -= room[2]

print(at_least_hp+1)