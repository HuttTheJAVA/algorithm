import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

matrix = []

shark_locate_matrix = [[[] for i in range(n)] for i in range(n)]

dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

for i in range(n):
    matrix.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            shark_locate_matrix[i][j].append(matrix[i][j])

scent_matrix = [[[0,0] for i in range(n)] for i in range(n)]

shark_x_y_coor = [0]*(m+1)

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            scent_matrix[i][j] = [k,matrix[i][j]]
            shark_x_y_coor[matrix[i][j]] = [i,j]

del(matrix)

shark_dir_lst = list(map(int,input().split()))

shark_dir_lst = [0] + shark_dir_lst

shark_priority_dir_dct = {}

for i in range(m):
    shark_priority_dir_dct[i+1] = [0]
    for j in range(4):
        dir_lst = list(map(int,input().split()))
        shark_priority_dir_dct[i+1].append(dir_lst)

shark_cnt = m

time = 0

while(shark_cnt != 1):
    for shark in range(1,len(shark_dir_lst)):
        if shark_dir_lst[shark]>0:
            my_x = None
            my_y = None
            shark_locate_matrix[shark_x_y_coor[shark][0]][shark_x_y_coor[shark][1]] = []
            for next_dir in shark_priority_dir_dct[shark][shark_dir_lst[shark]]:
                nx = shark_x_y_coor[shark][0] + dx[next_dir]
                ny = shark_x_y_coor[shark][1] + dy[next_dir]
                if 0<=nx<n and 0<=ny<n:
                    if scent_matrix[nx][ny][0]<=time:
                        my_x = nx
                        my_y = ny
                        shark_dir_lst[shark] = next_dir
                        break
                    elif scent_matrix[nx][ny][1] == shark:
                        if my_x == None:
                            my_x = nx
                            my_y = ny
                            shark_dir_lst[shark] = next_dir
                    
            shark_locate_matrix[my_x][my_y].append(shark)
            shark_x_y_coor[shark][0] = my_x
            shark_x_y_coor[shark][1] = my_y

    time += 1
    for i in range(n):
        for j in range(n):
            if len(shark_locate_matrix[i][j]) > 1:
                min_shark = 123123123
                min_dir = 12312312312
                shark_cnt -= len(shark_locate_matrix[i][j])-1
                for _ in range(len(shark_locate_matrix[i][j])):
                    next_shark = shark_locate_matrix[i][j].pop()
                    if next_shark < min_shark:
                        min_shark = next_shark
                        min_dir = shark_dir_lst[next_shark]
                    shark_dir_lst[next_shark] = 0
                shark_locate_matrix[i][j] = [min_shark]
                scent_matrix[i][j] = [time+k,min_shark]
                shark_dir_lst[min_shark] = min_dir
            elif len(shark_locate_matrix[i][j]) == 1:
                scent_matrix[i][j] = [time+k,shark_locate_matrix[i][j][0]]
    if time > 1000:
        break

if time <= 1000:
    print(time)
else:
    print(-1)