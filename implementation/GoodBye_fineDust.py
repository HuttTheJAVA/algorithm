import sys
input = sys.stdin.readline

r,c,t = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(r):
    matrix.append(list(map(int,input().split())))

top = [None,None]
bottom = [None,None]

t_dx = [0,-1,0,1]
t_dy = [1,0,-1,0]

b_dx = [0,1,0,-1]
b_dy = [1,0,-1,0]

def air_circulate(x,y,idx,buff,tmp,pos_dx,pos_dy):
    global matrix
    global r
    global c

    airCleaner_pos_x = x
    airCleaner_pos_y = y

    while(1):
        nx = x + pos_dx[idx]
        ny = y + pos_dy[idx]
        if nx == airCleaner_pos_x and ny == airCleaner_pos_y:
            break
        if 0<=nx<r and 0<=ny<c:
            if buff == None:
                buff = matrix[nx][ny]
                matrix[nx][ny] = 0
            else:
                tmp = matrix[nx][ny]
                matrix[nx][ny] = buff
                buff = tmp
            x = nx
            y = ny
        else:
            idx += 1
            nx = x + pos_dx[idx]
            ny = y + pos_dy[idx]
            if not (0<=nx<r and 0<=ny<c):
                break

for _ in range(t):
    add_matrix = [[0]*c for i in range(r)]
    cnt_matrix = [[0]*c for i in range(r)]
    for i in range(r): 
        for j in range(c):
            if matrix[i][j]>0:
                for idx in range(4):
                    nx = i + dx[idx]    
                    ny = j + dy[idx]    
                    if 0<=nx<r and 0<=ny<c and matrix[i][j]>0 and matrix[i][j]//5>0:
                        if matrix[nx][ny]>=0:
                            add_matrix[nx][ny] += matrix[i][j]//5
                            cnt_matrix[i][j] += 1
            elif matrix[i][j] == -1:
                if top[0] != None:
                    bottom[0] = i
                    bottom[1] = j
                else:
                    top[0] = i
                    top[1] = j

    for i in range(r):
        for j in range(c):
            matrix[i][j] -= (matrix[i][j]//5) * cnt_matrix[i][j]
            matrix[i][j] += add_matrix[i][j]
    
    air_circulate(top[0],top[1],0,None,None,t_dx,t_dy)

    air_circulate(bottom[0],bottom[1],0,None,None,b_dx,b_dy)

dust = 0

for i in range(r):
    for j in range(c):
        if matrix[i][j] > 0:
            dust += matrix[i][j]

print(dust)