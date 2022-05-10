import sys
import math as m
input = sys.stdin.readline

n = int(input())

jooun = list(map(int,input().split()))

boss = list(map(int,input().split()))

win_cnt = m.ceil((n+1)/2)

jooun.sort()

boss.sort(reverse=True)

joo_entry = jooun[:win_cnt]

joo_entry = joo_entry[::-1]

boss_entry = boss[:win_cnt]

cant = False

for i in range(len(joo_entry)):
    if joo_entry[i]>= boss[i]:
        cant = True
        break

if cant:
    print('NO')
else:
    print("YES")