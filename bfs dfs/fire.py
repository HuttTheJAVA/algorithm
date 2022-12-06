import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for _ in range(t):
    m,n = map(int,input().split()) # 열, 행 순으로 입력
    matrix = []

    for i in range(n):
        matrix.append(list(input().strip()))
    
    thedupp = deque()

    fire = deque()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "@":
                thedupp.append(((i,j),0))
            elif matrix[i][j] == '*':
                fire.append((i,j))
    escaped = False
    while(thedupp): # 이렇게 해도 되는지 제출전에 다시 확인해보자
        tmp_thedupp = deque()
        tmp_fire = deque()
        while(thedupp):
            im_thedupp,time = thedupp.popleft()     # (i,j) , 경과시간  형태
            for i in range(4):
                new_x = im_thedupp[0] + dx[i]
                new_y = im_thedupp[1] + dy[i]
                if 0<=new_x<n and 0<=new_y<m:
                    if matrix[new_x][new_y] == '.':
                        safe = True
                        for i in range(4):
                            new_new_x = new_x + dx[i]
                            new_new_y = new_y + dy[i]
                            if 0<=new_new_x<n and 0<=new_new_y<m:
                                if matrix[new_new_x][new_new_y] == '*':
                                    safe = False
                                    break
                        if safe:
                            matrix[new_x][new_y] = '@'
                            tmp_thedupp.append(((new_x,new_y),time+1))
                else:
                    print(time+1)
                    escaped = True
                    break
            if escaped:
                break
        if escaped:
            break
        thedupp = tmp_thedupp
        while(fire):
            im_fire = fire.popleft()
            for i in range(4):
                new_x = im_fire[0] + dx[i]
                new_y = im_fire[1] + dy[i]
                if 0<=new_x<n and 0<=new_y<m and matrix[new_x][new_y] != '*' and matrix[new_x][new_y] != '#':
                    matrix[new_x][new_y] = '*'
                    tmp_fire.append((new_x,new_y))
        fire = tmp_fire
    if not escaped:
        print("IMPOSSIBLE")