from collections import deque
import sys
input = sys.stdin.readline
saro,animal_cnt,L = map(int,input().split())

saro_lst = list(map(int,input().split()))

saro_lst.sort(reverse=True)

animal_coordinate = []

for i in range(animal_cnt):
    x,y = map(int,input().split())
    animal_coordinate.append((x,y,x+y))

animal_coordinate.sort(key=lambda x:(-x[2],-x[0],-x[1]))

cnt = 0

while(animal_coordinate and saro_lst):
    sx = saro_lst[-1]
    ax,ay,abs_dist = animal_coordinate[-1]
    if abs(ax-sx)+ay<=L:
        cnt += 1
        animal_coordinate.pop()
    elif sx <= ax:
        saro_lst.pop()
    else:
        animal_coordinate.pop()

print(cnt)