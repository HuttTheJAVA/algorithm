from collections import deque
import sys
input = sys.stdin.readline

n,m,gas = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

s_x,s_y = map(int,input().split())

s_x -= 1
s_y -= 1

guest_lst = []

for i in range(m):
    g_s_x,g_s_y,g_e_x,g_e_y = map(int,input().split())
    guest_lst.append((g_s_x-1,g_s_y-1,g_e_x-1,g_e_y-1))

done_guest = [0]*len(guest_lst)

serve_guest = len(guest_lst)

def calc_dist(s_x,s_y,e_x,e_y,calc_end):
    global n
    global guest_lst
    global done_guest
    global matrix
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    bfs_matrix = [[sys.maxsize]*n for i in range(n)]
    qu = deque()
    qu.append((s_x,s_y))
    bfs_matrix[s_x][s_y] = 0
    while(qu):
        x,y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if bfs_matrix[nx][ny] > bfs_matrix[x][y] + 1 and not matrix[nx][ny]:
                    bfs_matrix[nx][ny] = bfs_matrix[x][y] + 1
                    qu.append((nx,ny))
    
    if calc_end:
        if bfs_matrix[e_x][e_y] == sys.maxsize:
            return "cant"
        return e_x,e_y,bfs_matrix[e_x][e_y]

    min_dist = sys.maxsize
    min_guest_row = None
    min_guest_col = None
    min_guest_idx = None
    for guest_idx in range(len(guest_lst)):
        guest_x = guest_lst[guest_idx][0]
        guest_y = guest_lst[guest_idx][1]
        if bfs_matrix[guest_x][guest_y]<min_dist and not done_guest[guest_idx]:
            min_guest_idx = guest_idx
            min_guest_row = guest_x
            min_guest_col = guest_y
            min_dist = bfs_matrix[guest_x][guest_y]
        elif bfs_matrix[guest_x][guest_y] == min_dist and not done_guest[guest_idx]:
            if guest_x<min_guest_row:
                min_guest_idx = guest_idx
                min_guest_row = guest_x
                min_guest_col = guest_y
            elif guest_x == min_guest_row:
                if guest_y < min_guest_col:
                    min_guest_idx = guest_idx
                    min_guest_row = guest_x
                    min_guest_col = guest_y
    if min_guest_idx != None:
        return guest_lst[min_guest_idx][0],guest_lst[min_guest_idx][1],guest_lst[min_guest_idx][2],guest_lst[min_guest_idx][3],min_guest_idx,min_dist
    else:
        return "cant"

while(serve_guest):
    try:
        guest_s_x,guest_s_y,guest_e_x,guest_e_y,min_guest_idx,min_dist = calc_dist(s_x,s_y,None,None,0)
    except:
        gas = -1
        break
    if gas >= min_dist:
        gas -= min_dist
        s_x = guest_s_x
        s_y = guest_s_y
        try:
            e_x,e_y,end_dist = calc_dist(s_x,s_y,guest_e_x,guest_e_y,1)
        except:
            gas = -1
            break
        if gas>=end_dist:
            gas -= end_dist
            s_x = e_x
            s_y = e_y
            gas += 2*end_dist
            serve_guest -= 1
            done_guest[min_guest_idx] = 1
        else:
            gas = -1
            break
    else:
        gas = -1
        break

print(gas)