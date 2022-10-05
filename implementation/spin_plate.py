import sys
input = sys.stdin.readline

n,m,t = map(int,input().split()) # m은 꼭 4가 아님. 동서남북 이렇게만 적혀있지 않다.

platters = [[0]]

move_info = []

for i in range(n):
    platters.append(list(map(int,input().split())))

total_sum = 0  ## 원판 총합

cnt = 0

for i in range(1,n+1):
    for j in range(m):
        total_sum += platters[i][j]
        cnt += 1

for i in range(t):
    xi,di,ki = map(int,input().split())
    move_info.append((xi,di,ki))

def spin_platter(platter,clock_wise,times):
    times = times%len(platter)
    if not clock_wise:
        platter = platter[len(platter)-times:] + platter[:len(platter)-times]
    else:
        platter = platter[times:] + platter[:times]

    return platter

def calc_adj_i_j(i,j):
    global n
    global m
    lst = []

    i_up = None
    j_left = None
    i_down = None
    j_right = None
    if i-1<1:
        i_down = 51
    else:
        i_down = i-1
    if j-1<0:
        j_left = m-1
    else:
        j_left = j-1
    if i+1>n:
        i_up = 51
    else:
        i_up = i+1
    if j+1>=m:
        j_right = 0
    else:
        j_right = j+1
    
    return [(i_up,j),(i_down,j),(i,j_left),(i,j_right)]

for idx in range(len(move_info)):
    number = move_info[idx][0]  # 0부터 n-1까지
    clock_wise = move_info[idx][1]
    move_time = move_info[idx][2]
    for plat_num in range(1,len(platters)):
        if not plat_num%number:
            platters[plat_num] = spin_platter(platters[plat_num],clock_wise,move_time)
    at_least_once_change = False
    has_adj = set()
    for i in range(1,n+1):
        for j in range(m):
            change = False
            if platters[i][j] != '.':
                adj_lst = calc_adj_i_j(i,j)
                for x_y in adj_lst:
                    if 0<=x_y[0]<n+1 and 0<=x_y[1]<m and platters[i][j] == platters[x_y[0]][x_y[1]]:
                        has_adj.add((x_y[0],x_y[1]))
                        change = True
                        at_least_once_change = True
                if change:
                    has_adj.add((i,j))
    if not at_least_once_change:
        if cnt and total_sum:
            avg = total_sum/cnt
        else:
            break
        for i in range(1,n+1):
            for j in range(m):
                if platters[i][j] != '.':
                    if platters[i][j]>avg:
                        platters[i][j] -= 1
                        total_sum -= 1
                    elif platters[i][j]<avg:
                        platters[i][j] += 1
                        total_sum += 1
    else:
        has_adj = list(has_adj)
        for x_y in has_adj:
            total_sum -= platters[x_y[0]][x_y[1]]
            cnt -= 1
            platters[x_y[0]][x_y[1]] = '.'

print(total_sum)