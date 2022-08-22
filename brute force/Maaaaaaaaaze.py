import time
from collections import deque
import sys
input = sys.stdin.readline

matrix = []

INF = sys.maxsize
############################################################
already_done_dct = {}
flr_dct = {}

bit_flr = [0]*5

flr_lst = ['0','1','2','3','4']
def make_flr_combination(combi):
    global bit_flr
    global already_done_dct
    global flr_dct
    global flr_lst

    if len(combi) == 5:
        if combi not in already_done_dct:
            flr_dct[combi] = 1
            already_done_dct[combi[::-1]] = 1
        return

    for i in range(len(flr_lst)):
        if not bit_flr[i]:
            bit_flr[i] = 1
            make_flr_combination(combi+flr_lst[i])
            bit_flr[i] = 0

make_flr_combination("")
#######################################################
def clock_wise_maze_floor(matrix):

    copy_matrix = [[0]*5 for i in range(5)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            copy_matrix[j][abs(i-4)] = matrix[i][j]
    matrix = copy_matrix

    return matrix

shortest_path_cnt = INF

def search_path(stack_maze_lst):
    global shortest_path_cnt
    
    start = [(0,0,0),(0,0,4),(0,4,0),(0,4,4)]
    dz = [0,0,1,0,0,-1]
    dx = [1,0,0,0,-1,0]
    dy = [0,1,0,-1,0,0]

    for i in range(len(start)):
        maze_cnt = [[[sys.maxsize]*5 for i in range(5)] for i in range(5)]
        s = start[i]
        e = (abs(s[0]-4),abs(s[1]-4),abs(s[2]-4))
        qu = deque()
        if stack_maze_lst[s[0]][s[1]][s[2]]:
            maze_cnt[s[0]][s[1]][s[2]] = 0
            qu.append(s)
        
        while(qu):
            now_z,now_x,now_y = qu.popleft()
            if maze_cnt[e[0]][e[1]][e[2]] != INF:
                shortest_path_cnt = min(shortest_path_cnt,maze_cnt[e[0]][e[1]][e[2]])
                break
            for idx in range(6):
                new_z = now_z + dz[idx]
                new_x = now_x + dx[idx]
                new_y = now_y + dy[idx]
                if 0<=new_x<5 and 0<=new_y<5 and 0<=new_z<5 and stack_maze_lst[new_z][new_x][new_y]:
                    if maze_cnt[new_z][new_x][new_y] > maze_cnt[now_z][now_x][now_y]+1:
                        maze_cnt[new_z][new_x][new_y] = maze_cnt[now_z][now_x][now_y]+1
                        qu.append((new_z,new_x,new_y))
        return

for i in range(5):
    sub_matrix = []
    for j in range(5):
        line = list(map(int,input().split()))
        sub_matrix.append(line)
    matrix.append(sub_matrix)

start = [(0,0,0),(0,0,4),(0,4,0),(0,4,4)]

stack_maze_lst = []

on_stack = [0]*5

for k in flr_dct.keys():
    new_matrix = []
    for alp in k:
        new_matrix.append(matrix[int(alp)])

    for a in range(4):
        new_matrix[0] = clock_wise_maze_floor(new_matrix[0])
        for n in range(4):
            new_matrix[1] = clock_wise_maze_floor(new_matrix[1])
            for d in range(4):
                new_matrix[2] = clock_wise_maze_floor(new_matrix[2])
                for r in range(4):
                    new_matrix[3] = clock_wise_maze_floor(new_matrix[3])
                    for e in range(4):
                        new_matrix[4] = clock_wise_maze_floor(new_matrix[4])
                        search_path(new_matrix)

if shortest_path_cnt == INF:
    print(-1)
else:
    print(shortest_path_cnt)