import sys
from collections import deque
input = sys.stdin.readline

dx = [0,-1,-1,-1,0,1,1,1]   # ← 을 시작으로 반시계 방향

dy = [-1,-1,0,1,1,1,0,-1]

dir_2_num_dct = {2:'1',0:'2',6:'3',4:'4'}

turn = 1 # 이 변수는 전체 복제 시행 횟수 즉, 전체 단위 턴을 카운트한다. for문안에 들어가야됨.

def recursive_search(x,y,coor_lst,move_cnt,dir_number,eat_fish):
    global dx,dy,dir_2_num_dct,max_eat,move_dir_3,move_dir_2_number,visit
    if move_cnt == 3:
        dir_str = ''
        for alp in dir_number:
            dir_str += dir_2_num_dct[int(alp)]

        if eat_fish > max_eat:
            move_dir_3 = dir_number
            max_eat = eat_fish
            move_dir_2_number = dir_str
        elif eat_fish == max_eat:
            if int(dir_str)<int(move_dir_2_number):
                move_dir_3 = dir_number
                move_dir_2_number = dir_str
        return 
    for i in range(0,len(dx),2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<4 and 0<=ny<4: # 상어는 3번 까지 상하좌우 이동하므로 왕복 이동하지 않게만 구현하면 자기자신의 자리까지 올 일이 없다.
            if visit[nx][ny] == 1:
                recursive_search(nx,ny,coor_lst+[(nx,ny)],move_cnt+1,dir_number+str(i),eat_fish)
                # 중복으로 visit가 해제 될 수도 있지만, 어차피 해제만 되면 되므로 중복신경x  ## 디버깅해보니까 아니다 중복해제되면 미리 해제되는 경우 발생하므로 미리 해제하면 x recursive하게 탐색할 때 위배됨.
            else:
                visit[nx][ny] = 1
                if sx == nx and sy == ny:
                    recursive_search(nx,ny,coor_lst+[(nx,ny)],move_cnt+1,dir_number+str(i),eat_fish+(len(fish_and_shark_matrix[nx][ny])-1))
                else:
                    recursive_search(nx,ny,coor_lst+[(nx,ny)],move_cnt+1,dir_number+str(i),eat_fish+len(fish_and_shark_matrix[nx][ny]))
                visit[nx][ny] = 0

def transfer_dir(dir):
    if dir<0:
        return 7
    return dir

def move_fish():
    global scent_matrix,turn,sx,sy
    after_move_matrix = [[deque() for i in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            if fish_and_shark_matrix[i][j]:
                
                while(fish_and_shark_matrix[i][j]):
                    fish_dir = fish_and_shark_matrix[i][j][0]
                    if fish_dir != 8:
                        can = False
                        dir = fish_dir
                        for plus in range(8):
                            if not plus:
                                bia = 0
                            else:
                                bia = 1
                            dir = transfer_dir(dir-bia)
                            ni = i + dx[dir]
                            nj = j + dy[dir]
                            if 0<=ni<4 and 0<=nj<4 and not(ni==sx and nj==sy) and turn - scent_matrix[ni][nj]  > 2: #and 냄새 매트릭스에도 냄새의 값이 없거나 있어도 현재 turn보다 2이상 작으면.:
                                fish_and_shark_matrix[i][j].popleft() 
                                after_move_matrix[ni][nj].append(dir)   # 새로운 방향을 따로 배열의 새로운 칸에 저장
                                can = True
                                break
                        if not can: # 물고기가 8방향으로 갈수 없다는건 i,j칸의 모든 물고기들이 이동할수 없는 것이니 그대로 배열을 복사
                            # after_move_matrix[i][j] = fish_and_shark_matrix[i][j]
                            # fish_and_shark_matrix[i][j] = deque()
                            # break
                            after_move_matrix[i][j].append(fish_dir)
                            fish_and_shark_matrix[i][j].popleft()
                    else:
                        fish_and_shark_matrix[i][j].popleft()
                        after_move_matrix[i][j].append(8)
    return after_move_matrix

def copy_fish():
    copy_x_y_dir_lst = []
    for i in range(4):
        for j in range(4):
            if fish_and_shark_matrix[i][j]:
                for fish_dir in fish_and_shark_matrix[i][j]:
                    if fish_dir != 8:
                        copy_x_y_dir_lst.append((i,j,fish_dir))
    return copy_x_y_dir_lst


m,s = map(int,input().split())

fish_and_shark_matrix = [[deque() for i in range(4)] for i in range(4)]

for i in range(m):
    x,y,d = map(int,input().split())
    fish_and_shark_matrix[x-1][y-1].append(d-1)
    
sx,sy = map(int,input().split())
sx -= 1
sy -= 1

fish_and_shark_matrix[sx][sy].append(8) # 총 방향 인덱스는 7까지 있으므로 8이 있다면 이것은 상어를 뜻한다.시작 부터 상어 물고기를 겹치는 입력값으로 줄리는 없으니 일단append로 하자.
scent_matrix = [[-970623]*4 for i in range(4)]

visit = [[0]*4 for i in range(4)]

for i in range(s):
    max_eat = -1            # 이값은 복제 시행마다 최신화 돼야함.
    move_dir_3 = ''
    move_dir_2_number = ''
    copy_x_y_dir_lst = copy_fish()
    fish_and_shark_matrix = move_fish()
    recursive_search(sx,sy,[],0,'',0)
    fish_and_shark_matrix[sx][sy].popleft()
    for idx in move_dir_3:
        sx = sx + dx[int(idx)]
        sy = sy + dy[int(idx)]
        if fish_and_shark_matrix[sx][sy]:
            scent_matrix[sx][sy] = turn
            fish_and_shark_matrix[sx][sy] = deque()
    fish_and_shark_matrix[sx][sy].append(8)
    for x_y in copy_x_y_dir_lst:
        fish_and_shark_matrix[x_y[0]][x_y[1]].append(x_y[2])
    turn += 1

survive_cnt = 0

for i in range(4):
    for j in range(4):
        if fish_and_shark_matrix[i][j]:
            for f in fish_and_shark_matrix[i][j]:
                if f != 8:
                    survive_cnt += 1

print(survive_cnt)