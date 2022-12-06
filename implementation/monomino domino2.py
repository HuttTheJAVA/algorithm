import sys
input = sys.stdin.readline

n = int(input())

def return_green_n_blue_row_col(kind,x,y):      # 이 함수는 리스트 형태로 파란 영역과 초록 영역에 각각 시작해야할 칸들의 그룹을 캡슐화해 전달하는 함수
    blue_start_rows = []
    green_start_cols = []
    if kind == 1:
        blue_start_rows.append([x,1])
        green_start_cols.append([1,y])
    elif kind == 2:
        blue_start_rows.append([x,1])
        blue_start_rows.append([x,0])
        green_start_cols.append([1,y])
        green_start_cols.append([1,y+1])
    else:
        blue_start_rows.append([x,1])
        blue_start_rows.append([x+1,1])
        green_start_cols.append([1,y])
        green_start_cols.append([0,y])
    
    return green_start_cols,blue_start_rows

green = [[0]*4 for i in range(6)]
blue = [[0]*6 for i in range(4)]

score = 0

for _ in range(n):
    # print('go?')
    t,x,y = map(int,input().split())
    g_start_group,b_start_group = return_green_n_blue_row_col(t,x,y)

    for idx in range(len(g_start_group)):
        green[g_start_group[idx][0]][g_start_group[idx][1]] = 1
    for idx in range(len(b_start_group)):
        blue[b_start_group[idx][0]][b_start_group[idx][1]] = 1
    g_stop = False
    b_stop = False
    while(1):
        ok_go = True
        for idx in range(len(g_start_group)):
            if 0 <= g_start_group[idx][0] + 1 < 6 and not green[g_start_group[idx][0]+1][g_start_group[idx][1]]:
                continue
            elif 0 <= g_start_group[idx][0] + 1 < 6:
                if [g_start_group[idx][0]+1,g_start_group[idx][1]] not in g_start_group:
                    ok_go = False
                    g_stop = True
                    break
            else:
                ok_go = False
                g_stop = True
        if ok_go:
            for idx in range(len(g_start_group)):
                green[g_start_group[idx][0]][g_start_group[idx][1]] = 0
                green[g_start_group[idx][0]+1][g_start_group[idx][1]] = 1
                g_start_group[idx][0] += 1
        if g_stop:
            break
    
    occur_x = None
    del_line_cnt = 0
    for i in range(5,1,-1):                     # 일단 행은 5 ~ 2 까지만 확인 하고 0,1확인 하는 부분은 따로 아래에 구현하자.
        all_in_one = True
        for j in range(4):
            if not green[i][j]:
                all_in_one = False
        if all_in_one:
            occur_x = i
            del_line_cnt += 1
            score += 1
            for j in range(4):
                green[i][j] = 0     # 다 제거해버린다.

    
    if del_line_cnt:    # 만약 0,1칸에 블록 존재와 동시에 한 행이 꽉차는 경우가 발생해도 상관없는게 어차피 이러한 경우 한 행이 꽉찬 행이 맨위의 행 말고는 나올 경우가 없고 맨위(초록 2행)의 행이 사라져도 다른 행에 영향이 없다
        for i in range(occur_x-1,-1,-1):   # 5 ~ 2행 까지만 이동시킴
            for j in range(4):
                if green[i][j]:
                    green[i][j] = 0
                    green[i+del_line_cnt][j] = 1
                
    del_green_under_line = 0

    for i in range(2):
        for j in range(4):
            if green[i][j]:
                del_green_under_line += 1
                break
    
    for i in range(5,5-del_green_under_line,-1):
        for j in range(4):
            green[i][j] = 0
    if del_green_under_line:
        for i in range(5-del_green_under_line,-1,-1):     # 이때는 0,1행에 포함 돼있는 애들도 내려야함.
            for j in range(4):
                if green[i][j]:
                    green[i][j] = 0
                    green[i+del_green_under_line][j] = 1



    while(1):
        ok_go = True
        for idx in range(len(b_start_group)):
            if 0 <= b_start_group[idx][1] + 1 < 6 and not blue[b_start_group[idx][0]][b_start_group[idx][1]+1]:
                continue
            elif 0 <= b_start_group[idx][1] + 1 < 6:
                if [b_start_group[idx][0],b_start_group[idx][1]+1] not in b_start_group:
                    ok_go = False
                    b_stop = True
                    break
            else:
                ok_go = False
                b_stop = True
        if ok_go:
            for idx in range(len(b_start_group)):
                blue[b_start_group[idx][0]][b_start_group[idx][1]] = 0
                blue[b_start_group[idx][0]][b_start_group[idx][1]+1] = 1
                b_start_group[idx][1] += 1
        if b_stop:
            break
    
    occur_y = None
    del_line_cnt_blue = 0
    for j in range(5,1,-1):
        all_in_one = True
        for i in range(4):
            if not blue[i][j]:
                all_in_one = False
        if all_in_one:
            occur_y = j
            del_line_cnt_blue += 1
            score += 1
            for i in range(4):
                blue[i][j] = 0
    
    if del_line_cnt_blue:
        for j in range(occur_y-1,-1,-1):
            for i in range(4):
                if blue[i][j]:
                    blue[i][j] = 0
                    blue[i][j+del_line_cnt_blue] = 1
    
    del_blue_under_line = 0

    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                del_blue_under_line += 1
                break
    
    for j in range(5,5-del_blue_under_line,-1):
        for i in range(4):
            blue[i][j] = 0
    if del_blue_under_line:
        for j in range(5-del_blue_under_line,-1,-1):
            for i in range(4):
                if blue[i][j]:
                    blue[i][j] = 0
                    blue[i][j+del_blue_under_line] = 1

print(score)

cnt_blocks = 0

for i in range(2,6):
    for j in range(4):
        if green[i][j]:
            cnt_blocks += 1

for i in range(4):
    for j in range(2,6):
        if blue[i][j]:
            cnt_blocks += 1

print(cnt_blocks)