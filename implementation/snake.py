import sys
input = sys.stdin.readline

L = int(input())

n = int(input())

snake_row = 0
snake_col = 0
dir = 0
snake_ranges = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]

def change_dir(dir,turn):
    if turn == 'L':
        dir -= 1
    else:
        dir += 1

    if dir < 0:
        dir = 3
    elif dir > 3:
        dir = 0
    
    return dir

die_cnt = 0
collision_len = sys.maxsize
dead = False
for i in range(n):
    move,turn = input().split()
    move = int(move)
    if collision_len == sys.maxsize:
        new_snake_row = snake_row + dy[dir]*move # 전의 뱀의 방향과 경과된 시간 곱함.
        new_snake_col = snake_col + dx[dir]*move
        for x_y in snake_ranges:         # x_y = [[(y1,x1),(y2,x2)],[...],...]
            y1,x1,y2,x2 = x_y[0][0],x_y[0][1],x_y[1][0],x_y[1][1]
            
            if y1<=snake_row<=y2 and snake_col<x1 and new_snake_col>=x1:
                collision_len = min(collision_len,x1-snake_col)

            elif x1<=snake_col<=x2 and snake_row<y1 and new_snake_row>=y1:
                collision_len = min(collision_len,y1-snake_row)

            elif y1<=snake_row<=y2 and snake_col>x1 and new_snake_col<=x1:
                collision_len = min(collision_len,snake_col - x1)

            elif x1<=snake_col<=x2 and snake_row>y1 and new_snake_row<=y1:
                collision_len = min(collision_len,snake_row - y1)

        if not(-L<=new_snake_row<=L and -L<=new_snake_col<=L):
            if abs(new_snake_row)>abs(L):
                minus_move = abs(new_snake_row) - (abs(L)+1)
            elif abs(new_snake_col)>abs(L):
                minus_move = abs(new_snake_col) - (abs(L)+1)
            collision_len = min(collision_len,move - minus_move)

        if collision_len == sys.maxsize:
            new_range = [(snake_row,snake_col),(new_snake_row,new_snake_col)]
            new_range.sort(key=lambda x:(x[0],x[1]))
            snake_ranges.append(new_range)
            dir = change_dir(dir,turn)
            die_cnt += move
            snake_col = new_snake_col
            snake_row = new_snake_row
        else:
            die_cnt += collision_len
move = 10**9
if collision_len == sys.maxsize:
    new_snake_col = snake_col + move*dx[dir]
    new_snake_row = snake_row + move*dy[dir]
    for x_y in snake_ranges:         # x_y = [[(y1,x1),(y2,x2)],[...],...]
        y1,x1,y2,x2 = x_y[0][0],x_y[0][1],x_y[1][0],x_y[1][1]
        
        if y1<=snake_row<=y2 and snake_col<x1 and new_snake_col>=x1:
            collision_len = min(collision_len,x1-snake_col)

        elif x1<=snake_col<=x2 and snake_row<y1 and new_snake_row>=y1:
            collision_len = min(collision_len,y1-snake_row)

        elif y1<=snake_row<=y2 and snake_col>x1 and new_snake_col<=x1:
            collision_len = min(collision_len,snake_col - x1)

        elif x1<=snake_col<=x2 and snake_row>y1 and new_snake_row<=y1:
            collision_len = min(collision_len,snake_row - y1)

    if collision_len == sys.maxsize:
        if not(-L<=new_snake_row<=L and -L<=new_snake_col<=L):
            if abs(new_snake_row)>abs(L):
                minus_move = abs(new_snake_row) - (abs(L)+1)
            elif abs(new_snake_col)>abs(L):
                minus_move = abs(new_snake_col) - (abs(L)+1)
            collision_len =  min(collision_len,move - minus_move)
    die_cnt += collision_len        
print(die_cnt)