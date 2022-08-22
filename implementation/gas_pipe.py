import sys
input = sys.stdin.readline

r,c = map(int,input().split())

matrix = []

for i in range(r):
    matrix.append(list(input().strip()))

mouth_2_close = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]

pipe_lst = ['|','-','+','1','2','3','4']

pipe_dir_dct = {
    '|':['x','o','x','o'],
    '-':['o','x','o','x'],
    '+':['o','o','o','o'],
    '1':['o','o','x','x'],
    '2':['o','x','x','o'],
    '3':['x','x','o','o'],
    '4':['x','o','o','x']
}

pipe_compatibility_dct = {
    0:['-','+','3','4','M','Z'],
    1:['|','+','2','3','M','Z'],
    2:['-','+','1','2','M','Z'],
    3:['|','+','1','4','M','Z']
    }

need_2_close_x = None
need_2_close_y = None

for i in range(r):                      # 밀폐해야할 파이프 주둥이 수 구하는 코드 및 소실된 파이프의 좌표값을 찾아주는 코드 (모든 파이프를 순회해 밀폐가 만족되지 않는 소실 좌표임.)
    for j in range(c):
        if not (matrix[i][j] == 'M' or matrix[i][j] == 'Z' or matrix[i][j] == '.'):
            init_mouth_2_close = 0
            if matrix[i][j] == '+':
                mouth_2_close += 4
            else:
                mouth_2_close += 2
            if need_2_close_x == None and need_2_close_y == None:
                for idx in range(4):
                    if pipe_dir_dct[matrix[i][j]][idx] == "o":
                        nx = i + dx[idx]
                        ny = j + dy[idx]
                        if 0<=nx<r and 0<=ny<c:
                            if matrix[nx][ny] in pipe_compatibility_dct[idx]:
                                init_mouth_2_close += 1
                            else:
                                need_2_close_x = nx
                                need_2_close_y = ny
                                break

for pipe in pipe_lst:
    if pipe == '+':
        amount = 4
    else:
        amount = 2
    mouth_2_close += amount
    tmp = mouth_2_close
    matrix[need_2_close_x][need_2_close_y] = pipe
    so_far_so_good = True
    for i in range(r):
        for j in range(c):
            if not (matrix[i][j] == 'M' or matrix[i][j] == 'Z' or matrix[i][j] == '.'):
                for idx in range(4):
                    if pipe_dir_dct[matrix[i][j]][idx] == "o":
                        nx = i + dx[idx]
                        ny = j + dy[idx]
                        if 0<=nx<r and 0<=ny<c:
                            if matrix[nx][ny] not in pipe_compatibility_dct[idx]:
                                so_far_so_good = False
                                break
                            else:
                                mouth_2_close -= 1
            if not so_far_so_good:
                break
        if not so_far_so_good:
            break
    if not mouth_2_close:
        print(need_2_close_x+1,need_2_close_y+1,pipe)
        break
    else:
        mouth_2_close = tmp - amount
        matrix[need_2_close_x][need_2_close_y] = '.'