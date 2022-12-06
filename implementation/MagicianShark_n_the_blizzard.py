import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
## 얼음파편 방향과 dx,dy방향 동기화 시켜야됨 그리고 -1씩 해줘야 0인덱스부터 맞춰짐.#############
dx = [0,1,0,-1]
dy = [1,0,-1,0]
matrix = []

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

blizzard = []

for i in range(m):
    a,b = map(int,input().split())
    blizzard.append((a,b))

def turn(dir):
    if dir < 0:
        return 3
    return dir

distroy_score = 0

def add_score(num,leng):
    global distroy_score
    if num == 1:
        distroy_score += 1*leng
    elif num == 2:
        distroy_score += 2*leng
    else:
        distroy_score += 3*leng

def tornado_search(case):#case1 = 빈칸 채우기,case2 = 연속 구슬세고 4칸이상 파괴,case3 == 구슬 집합 크기 세기
    global matrix
    now_x = (n+1)//2-1
    now_y = (n+1)//2-1
    stack = 1
    dir = 2
    end = False
    empty_stack = deque()
    if case == 1:
        while(not end):
            for i in range(2):
                for w in range(1,stack+1):
                    nx = now_x + dx[dir]
                    ny = now_y + dy[dir]
                    if 0<=nx<n and 0<=ny<n:
                        if matrix[nx][ny]:
                            if empty_stack:
                                old_x,old_y = empty_stack.popleft()
                                matrix[old_x][old_y] = matrix[nx][ny]
                                matrix[nx][ny] = 0
                                empty_stack.append((nx,ny))
                                empty_spot = True
                        else:
                            empty_stack.append((nx,ny))
                        
                        now_x = nx
                        now_y = ny
                    else:
                        end = True
                        break
                if end:
                    break
                dir = turn(dir-1)
            if end:
                break
            stack += 1
    elif case == 2:
        empty_spot = False
        prev = None
        over_4 = []
        while(not end):
            for i in range(2):
                for w in range(1,stack+1):
                    nx = now_x + dx[dir]
                    ny = now_y + dy[dir]
                    if 0<=nx<n and 0<=ny<n:
                        if matrix[nx][ny]:
                            if prev == None:
                                prev = matrix[nx][ny]
                                over_4.append((nx,ny))
                            elif matrix[nx][ny] == prev:
                                over_4.append((nx,ny))
                            elif matrix[nx][ny] != prev:
                                if len(over_4)>=4:
                                    empty_spot = True
                                    for member in over_4:
                                        matrix[member[0]][member[1]] = 0
                                    add_score(prev,len(over_4))
                                        
                                prev = matrix[nx][ny]
                                over_4 = [(nx,ny)]
                        else:
                            if len(over_4)>=4:
                                empty_spot = True
                                for member in over_4:
                                    matrix[member[0]][member[1]] = 0
                                add_score(prev,len(over_4))
                            prev = None
                            over_4 = []
                
                        now_x = nx
                        now_y = ny
                    else:
                        end = True
                        break
                if end:
                    break
                dir = turn(dir-1)
            if end:
                break
            stack += 1
        if len(over_4) >= 4:
            for member in over_4:
                matrix[member[0]][member[1]] = 0
        return empty_spot
    else:
        new_matrix = [[0]*n for i in range(n)]
        group_cnt_n_num = deque()
        over_4 = []
        prev = None
        while(not end):
            for i in range(2):
                for w in range(1,stack+1):
                    nx = now_x + dx[dir]
                    ny = now_y + dy[dir]
                    if 0<=nx<n and 0<=ny<n:
                        if matrix[nx][ny]:
                            if prev == None and matrix[nx][ny]:
                                prev = matrix[nx][ny]
                                over_4.append((nx,ny))
                            elif matrix[nx][ny] == prev:
                                over_4.append((nx,ny))
                            elif matrix[nx][ny] != prev:
                                group_cnt_n_num.append(len(over_4))
                                group_cnt_n_num.append(prev)
                                prev = matrix[nx][ny]
                                over_4 = [(nx,ny)]
                        elif not matrix[nx][ny]:
                            if over_4:
                                group_cnt_n_num.append(len(over_4))
                                group_cnt_n_num.append(prev)
                            end = True 
                            break
                        
                        now_x = nx
                        now_y = ny
                    else:
                        end = True
                        break
                if end:
                    break
                dir = turn(dir-1)
            if end:
                break
            stack += 1
        now_x = (n+1)//2-1
        now_y = (n+1)//2-1
        stack = 1
        dir = 2
        end = False
        while(not end and group_cnt_n_num):
            for i in range(2):
                for w in range(1,stack+1):
                    nx = now_x + dx[dir]
                    ny = now_y + dy[dir]
                    if 0<=nx<n and 0<=ny<n:
                        if group_cnt_n_num:
                            new_matrix[nx][ny] = group_cnt_n_num.popleft()
                        else:
                            end = True
                        now_x = nx
                        now_y = ny
                    else:
                        end = True
                        break
                if end:
                    break
                dir = turn(dir-1)
            if end:
                break
            stack += 1
        return new_matrix

dir_dct = {1:3,2:1,3:2,4:0}

for spell in blizzard:
    direction = dir_dct[spell[0]]
    distance = spell[1]
    x = (n+1)//2 - 1
    y = x
    for i in range(1,distance+1):
        nx = x + dx[direction]*i
        ny = y + dy[direction]*i
        if 0<=nx<n and 0<=ny<n:
            matrix[nx][ny] = 0
        
    while(1):
        tornado_search(1)
        if not tornado_search(2):
            break
    matrix = tornado_search(3)

print(distroy_score)