import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))

yut_board = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,'end',22,23,24,30,26,24,28,29,24,31,20]
yut_score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,22,24,28,27,26,30,35]

is_blue = {5:21,10:25,15:27}

horse_location = [0,0,0,0]

max_score = 0

def move_horse(score,horse_location,idx,move_lst):
    global lst
    global max_score
    if idx<len(lst):
        move = lst[idx]
    else:
        max_score = max(max_score,score)
        return

    for horse_idx in range(len(horse_location)):
        if horse_location[horse_idx] != 'end':
            init_location = horse_location[horse_idx]
            now_location = horse_location[horse_idx]
            init_move = move
            if now_location in is_blue and move:
                now_location = is_blue[now_location]
                move -= 1
            while(move):
                now_location = yut_board[now_location]
                move -= 1
                if now_location == 'end':
                    break
            if now_location == 'end' or now_location not in horse_location:
                horse_location[horse_idx] = now_location
                if now_location != 'end':
                    move_horse(score + yut_score[now_location],horse_location,idx+1,move_lst)
                else:
                    move_horse(score,horse_location,idx+1,move_lst)
                horse_location[horse_idx] = init_location
            move = init_move

move_horse(0,horse_location,0,[])

print(max_score)