import sys
import copy
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

min_lean_time = 11
def lean_matrix(R_B_x_y_lst,dir,lean_time,now_matrix):
    global n
    global m
    global min_lean_time
    if lean_time > 10 or lean_time >= min_lean_time:
        return
    R_out = False
    B_out = False
    if dir == 0:
        R_B_x_y_lst.sort(key=lambda x:(x[1],x[0])) # 더 오른쪽에 있는(열이 더 큰)구슬이 뒤로오게 pop
    elif dir == 1:
        R_B_x_y_lst.sort(key=lambda x:(x[0],x[1])) # 더 아래쪽에 있는(행이 더 큰)구슬이 뒤로오게 pop
    elif dir == 2:
        R_B_x_y_lst.sort(key=lambda x:(-x[1],x[0])) # 더 왼쪽에 있는(열이 더 작은)구슬이 뒤로오게 pop
    elif dir == 3:
        R_B_x_y_lst.sort(key=lambda x:(-x[0],x[1])) # 더 위쪽에 있는(행이 더 작은)구슬이 뒤로오게 pop
    
    final_R_B_x_y_lst = []

    while(R_B_x_y_lst):
        X,Y,Color = R_B_x_y_lst.pop()
        tmp_X = X
        tmp_Y = Y
        while(1):
            NX = X + dx[dir]
            NY = Y + dy[dir]
            if 0<=NX<n and 0<=NY<m:
                if now_matrix[NX][NY] == '.':
                    X = NX
                    Y = NY
                elif now_matrix[NX][NY] == 'O':
                    if Color == 'R':
                        R_out = True
                        now_matrix[tmp_X][tmp_Y] = '.'
                        break
                    elif Color == 'B':
                        B_out = True
                        break
                else:
                    break
            else:
                break
        if not(tmp_X == X and tmp_Y == Y):
            if Color == 'R':
                if not R_out:
                    R_change = True
                    now_matrix[X][Y] = Color
                    now_matrix[tmp_X][tmp_Y] = '.'
            else:
                if not B_out:
                    now_matrix[X][Y] = Color
                    now_matrix[tmp_X][tmp_Y] = '.'

        final_R_B_x_y_lst.append((X,Y,Color))
    if R_out and not B_out:
        min_lean_time = min(min_lean_time,lean_time)   #### 기울이는 움직임이 선 반영된 카운트
        return
    elif B_out:
        return
    tmp_matrix = copy.deepcopy(now_matrix)
    tmp_final_R_B_x_y_lst = copy.deepcopy(final_R_B_x_y_lst)
    for direction in range(4):
        if direction != dir and (direction+2)%4 != dir:
            lean_matrix(final_R_B_x_y_lst,direction,lean_time+1,now_matrix)
            now_matrix = copy.deepcopy(tmp_matrix)
            final_R_B_x_y_lst = copy.deepcopy(tmp_final_R_B_x_y_lst)

for i in range(n):
    matrix.append(list(input().strip()))

R_x = None
R_y = None
B_x = None
B_y = None

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            R_x = i
            R_y = j
        elif matrix[i][j] == 'B':
            B_x = i
            B_y = j

tmp_matrix = copy.deepcopy(matrix)
for dir in range(4):
    lean_matrix([[R_x,R_y,'R'],[B_x,B_y,'B']],dir,1,matrix)
    matrix = copy.deepcopy(tmp_matrix)

if min_lean_time<=10:
    print(min_lean_time)
else:
    print(-1)