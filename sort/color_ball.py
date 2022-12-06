from collections import deque
from itertools import accumulate
import sys

input = sys.stdin.readline

n = int(input())


lst = []

max_col = -1

for i in range(n):
    c,s = map(int,input().split())
    max_col = max(max_col,c)
    lst.append((c,s,i+1))

color = [0]*(max_col+1)

lst.sort(key=lambda x:(x[1],x[0],x[2]))

lst = deque(lst)

accumulate_ball = 0

new_lst = []

color_biggest_size_and_count = [[0,0] for i in range(max_col+1)]

recent_size = -1
recent_accumulate = 0
recent_color = -1

while(lst):
    c,s,i = lst.popleft()
    if recent_size == -1:
        new_lst.append((c,s,0,i))
        recent_accumulate = 0
    elif s>recent_size:
        new_lst.append((c,s,accumulate_ball-color[c],i))
        recent_accumulate = accumulate_ball-color[c]
    else:
        if s == color_biggest_size_and_count[c][0]:
            new_lst.append((c,s,recent_accumulate+(color[recent_color]-color_biggest_size_and_count[recent_color][0]*color_biggest_size_and_count[recent_color][1])-(color[c]-color_biggest_size_and_count[c][0]*color_biggest_size_and_count[c][1]),i))
            recent_accumulate = recent_accumulate+(color[recent_color]-color_biggest_size_and_count[recent_color][0]*color_biggest_size_and_count[recent_color][1])-(color[c]-color_biggest_size_and_count[c][0]*color_biggest_size_and_count[c][1])
        else:
            new_lst.append((c,s,recent_accumulate+(color[recent_color]-color_biggest_size_and_count[recent_color][0]*color_biggest_size_and_count[recent_color][1])-color[c],i))
            recent_accumulate = recent_accumulate+(color[recent_color]-color_biggest_size_and_count[recent_color][0]*color_biggest_size_and_count[recent_color][1])-color[c]
    accumulate_ball += s # 바깥으로 빼자
    recent_color = c  # 바깥으로 빼자
    recent_size = s #바깥으로 빼자
    color[c] += s # 바깥으로 빼자
    if color_biggest_size_and_count[c][0]<s:
        color_biggest_size_and_count[c] = [s,1]
    else:
        color_biggest_size_and_count[c][1] += 1


new_lst.sort(key=lambda x:x[3])

for i in new_lst:
    print(i[2])
