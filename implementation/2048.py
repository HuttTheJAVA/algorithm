import sys
import copy
input = sys.stdin.readline

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

max_block = 0

for i in range(n):
    for j in range(n):
        max_block = max(max_block,matrix[i][j])

def recursive_move(changeable_move_matrix,sweep_dir,move_cnt,combi):
    global n
    global max_block
    if move_cnt == 5:
        for i in range(n):
            for j in range(n):
                max_block = max(max_block,changeable_move_matrix[i][j])
        return
    if sweep_dir == 0:
        compress_dir = (sweep_dir + 2)%4
        for i in range(n-1,-1,-1):
            for j in range(n):
                if changeable_move_matrix[j][i]:
                    # # # # # # # # # # # # # # # # # # # # # # # # 
                    x = j
                    y = i
                    while(1):
                        nx = x + dx[compress_dir]
                        ny = y + dy[compress_dir]
                        if 0<=nx<n and 0<=ny<n:
                            if changeable_move_matrix[nx][ny]:
                                if changeable_move_matrix[nx][ny] == changeable_move_matrix[j][i]:
                                    changeable_move_matrix[j][i] *= 2
                                    changeable_move_matrix[nx][ny] = 0
                                    break
                                else:
                                    break
                            else:
                                x = nx 
                                y = ny
                        else:
                            break
                    # # # # # # # # # # # # # # # # # # # # # # # #    
                    x = j
                    y = i
                    while(1):
                        nx = x + dx[sweep_dir]
                        ny = y + dy[sweep_dir]
                        if 0<=nx<n and 0<=ny<n and changeable_move_matrix[nx][ny] == 0:
                            x = nx
                            y = ny
                        else:
                            break
                    changeable_move_matrix[x][y] = changeable_move_matrix[j][i]
                    if not(x==j and y==i):
                        changeable_move_matrix[j][i] = 0

    elif sweep_dir == 1:
        compress_dir = (sweep_dir + 2)%4
        for i in range(n-1,-1,-1):
            for j in range(n):
                if changeable_move_matrix[i][j]:
                    x = i
                    y = j
                    while(1):
                        nx = x + dx[compress_dir]
                        ny = y + dy[compress_dir]
                        if 0<=nx<n and 0<=ny<n:
                            if changeable_move_matrix[nx][ny]:
                                if changeable_move_matrix[nx][ny] == changeable_move_matrix[i][j]:
                                    changeable_move_matrix[i][j] *= 2
                                    changeable_move_matrix[nx][ny] = 0
                                    break
                                else:
                                    break
                            else:
                                x = nx
                                y = ny
                        else:
                            break
            
                    x = i
                    y = j
                    while(1):
                        nx = x + dx[sweep_dir]
                        ny = y + dy[sweep_dir]
                        if 0<=nx<n and 0<=ny<n and changeable_move_matrix[nx][ny] == 0:
                            x = nx
                            y = ny
                        else:
                            break
                    changeable_move_matrix[x][y] = changeable_move_matrix[i][j]
                    if not(x == i and y == j):
                        changeable_move_matrix[i][j] = 0
    elif sweep_dir == 2:
        compress_dir = (sweep_dir + 2)%4
        for i in range(n):
            for j in range(n):
                if changeable_move_matrix[j][i]:
                    x = j
                    y = i
                    while(1):
                        nx = x + dx[compress_dir]
                        ny = y + dy[compress_dir]
                        if 0<=nx<n and 0<=ny<n:
                            if changeable_move_matrix[nx][ny]:
                                if changeable_move_matrix[nx][ny] == changeable_move_matrix[j][i]:
                                    changeable_move_matrix[j][i] *= 2
                                    changeable_move_matrix[nx][ny] = 0
                                    break
                                else:
                                    break
                            else:
                                x = nx
                                y = ny
                        else:
                            break
                    x = j
                    y = i
                    while(1):
                        nx = x + dx[sweep_dir]
                        ny = y + dy[sweep_dir]
                        if 0<=nx<n and 0<=ny<n and changeable_move_matrix[nx][ny] == 0:
                            x = nx
                            y = ny
                        else:
                            break
                    changeable_move_matrix[x][y] = changeable_move_matrix[j][i]
                    if not(x==j and y == i):
                        changeable_move_matrix[j][i] = 0
    elif sweep_dir == 3:
        compress_dir = (sweep_dir + 2)%4
        for i in range(n):
            for j in range(n):
                if changeable_move_matrix[i][j]:
                    x = i
                    y = j
                    while(1):
                        nx = x + dx[compress_dir]
                        ny = y + dy[compress_dir]
                        if 0<=nx<n and 0<=ny<n:
                            if changeable_move_matrix[nx][ny]:
                                if changeable_move_matrix[nx][ny] == changeable_move_matrix[i][j]:
                                    changeable_move_matrix[i][j] *= 2
                                    changeable_move_matrix[nx][ny] = 0
                                    break
                                else:
                                    break
                            else:
                                x = nx
                                y = ny
                        else:
                            break
                    x = i
                    y = j
                    while(1):
                        nx = x + dx[sweep_dir]
                        ny = y + dy[sweep_dir]
                        if 0<=nx<n and 0<=ny<n and changeable_move_matrix[nx][ny] == 0:
                            x = nx
                            y = ny
                        else:
                            break
                    changeable_move_matrix[x][y] = changeable_move_matrix[i][j]
                    if not(x==i and y == j):
                        changeable_move_matrix[i][j] = 0

    tmp = copy.deepcopy(changeable_move_matrix)
    for direction in range(4):
        recursive_move(changeable_move_matrix,direction,move_cnt+1,combi+str(sweep_dir))
        changeable_move_matrix = copy.deepcopy(tmp)

copy_matrix = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        copy_matrix[i][j] == matrix[i][j]

tmp = copy.deepcopy(matrix)
for i in range(4):
    recursive_move(matrix,i,0,"")
    matrix = copy.deepcopy(tmp)
print(max_block)