import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)
garbage_coor = []

for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            garbage_coor.append((i,j))

garbage_coor.sort(key=lambda x:(x[0],x[1]))

garbage_coor = deque(garbage_coor)

cnt = 0
while(garbage_coor):
    now_x,now_y = garbage_coor.popleft()
    cnt += 1
    new_garbage_coor = deque()
    while(garbage_coor):
        next_x,next_y = garbage_coor.popleft()
        if next_x >= now_x and next_y >= now_y:
            now_x = next_x
            now_y = next_y
            continue
        else:
            new_garbage_coor.append((next_x,next_y))
    garbage_coor = new_garbage_coor

print(cnt)