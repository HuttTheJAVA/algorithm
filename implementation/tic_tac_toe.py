import sys
input = sys.stdin.readline

def check_horizontal(matrix,x_made,o_made):
    global x_set
    global o_set
    for i in range(0,7,3):
        new_lst = []
        if matrix[i] != '.':
            pivot = matrix[i]
            made = True
            for j in range(i,i+3):
                if matrix[j] != pivot:
                    made = False
                    break
                else:
                    new_lst.append(j)
            if made:
                if pivot == 'X':
                    x_made += 1
                    for val in new_lst:
                        x_set.add(val)
                else:
                    o_made += 1
                    for val in new_lst:
                        o_set.add(val)
    return x_made,o_made

def check_vertical(matrix,x_made,o_made):
    global x_set
    global o_set
    for i in range(3):
        if matrix[i] != '.':
            new_lst = []
            pivot = matrix[i]
            made = True
            for j in range(i,i+3*2+1,3):
                if matrix[j] != pivot:
                    made = False
                    break
                else:
                    new_lst.append(j)
            if made:
                if pivot == 'X':
                    x_made += 1
                    for val in new_lst:
                        x_set.add(val)
                else:
                    o_made += 1
                    for val in new_lst:
                        o_set.add(val)
    return x_made,o_made    

def check_diagonal(matrix,x_made,o_made):
    global x_set
    global o_set
    if matrix[0] != '.':
        pivot = matrix[0]
        made = True
        new_lst = []
        for i in range(0,9,4):
            if matrix[i] != pivot:
                made = False
                break
            else:
                new_lst.append(i)
        if made:
            if pivot == 'X':
                x_made += 1
                for val in new_lst:
                    x_set.add(val)
            else:
                o_made += 1
                for val in new_lst:
                    o_set.add(val)

    if matrix[2] != '.':
        pivot = matrix[2]
        made = True
        new_lst = []
        for i in range(2,7,2):
            if matrix[i] != pivot:
                made = False
                break
            else:
                new_lst.append(i)
        if made:
            if pivot == 'X':
                x_made += 1
                for val in new_lst:
                    x_set.add(val)
            else:
                o_made += 1
                for val in new_lst:
                    o_set.add(val)
    
    return x_made,o_made
        

while(1):
    x_set = set()
    o_set = set()
    word = input().strip()
    if word == 'end':
        break
    board = list(word)
    x_cnt = 0
    o_cnt = 0
    dot_cnt = 0
    x_made = 0
    o_made = 0
    for i in range(len(board)):
        if board[i] == 'X':
            x_cnt += 1
        elif board[i] == 'O':
            o_cnt += 1
        else:
            dot_cnt += 1
    if x_cnt>o_cnt and abs(x_cnt - o_cnt) == 1 or x_cnt == o_cnt: # x o 차이가 x 가 더 많고 1차이이거나(칸이 꽉차게 무승부거나 x가 이긴 경우 둘중 하나) 둘다 같거나(이 경우 o가 이긴 상황만 같을 수 있음.)
        x_plus,o_plus = check_horizontal(board,0,0)
        x_plus2,o_plus2 = check_diagonal(board,0,0)
        x_plus3,o_plus3 = check_vertical(board,0,0)
        x_made = x_plus+x_plus2+x_plus3
        o_made = o_plus+o_plus2+o_plus3
        if x_cnt > o_cnt:
            if x_made == 2 and not o_made:
                if len(x_set) == 5:
                    print('valid')
                else:
                    print('invalid')
            elif x_made == 1 and not o_made:
                if len(x_set) == 3:
                    print('valid')
                else:
                    print('invalid')
            elif not x_made and not o_made and not dot_cnt:
                print('valid')
            else:
                print('invalid')
        elif x_cnt == o_cnt:
            if not x_made:
                if len(o_set) == 3:
                    print('valid')
                else:
                    print('invalid')
            else:
                print('invalid')
    else:
        print('invalid')