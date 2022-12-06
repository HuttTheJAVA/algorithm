import sys
from collections import deque
input = sys.stdin.readline

face_2_color = {'L':'G','U':'W','D':'Y','F':'R','B':'O','R':'B'}

clock_wise_spin = {'W':[['R','T'],['G','T'],['O','U'],['B','T'],['R','T']],
                   'R':[['W','U'],['B','L'],['Y','T'],['G','R'],['W','U']],
                   'B':[['W','R'],['O','R'],['Y','R'],['R','R'],['W','R']],
                   'O':[['W','T'],['G','L'],['Y','U'],['B','R'],['W','T']],
                   'G':[['W','L'],['R','L'],['Y','L'],['O','L'],['W','L']],
                   'Y':[['O','T'],['G','U'],['R','U'],['B','U'],['O','T']]}

def spin_face(color,dir):
    global cube
    if dir == '+':
        new_face = [['0']*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                new_face[j][2-i] = cube[color][i][j]
        cube[color] = new_face
    else:
        new_face = [['0']*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                new_face[2-j][i] = cube[color][i][j]
        cube[color] = new_face

def change_elements(input_lst,prev_color,color,LRUT):
    tmp_lst = []
    if prev_color == 'O' and (color == 'G' or color == 'B'):
        input_lst = input_lst[::-1]
    elif (prev_color == 'G' or prev_color == 'B') and color == 'O':
        input_lst = input_lst[::-1]
    elif prev_color == 'W' and color == 'G':
        input_lst = input_lst[::-1]
    elif prev_color == 'G' and color == 'W':
        input_lst = input_lst[::-1]
    elif prev_color == 'Y' and color == 'B':
        input_lst = input_lst[::-1]
    elif prev_color == 'B' and color == 'Y':
        input_lst = input_lst[::-1]
    if LRUT == 'L' or LRUT == 'R':
        if LRUT == 'L':
            col = 0
        else:
            col = 2
        for i in range(3):
            tmp_lst.append(cube[color][i][col])
            if input_lst:
                cube[color][i][col] = input_lst[i]
    else:
        if LRUT == 'T':
            row = 0
        else:
            row = 2
        for i in range(3):
            tmp_lst.append(cube[color][row][i])
            if input_lst:
                cube[color][row][i] = input_lst[i]
    return tmp_lst 

def spin_adj_faces(color,dir):
    global clock_wise_spin,TRUL_state
    if dir == '+':
        order = clock_wise_spin[color]
    else:
        order = clock_wise_spin[color][::-1]
    
    init_color = None
    prev_lst = []
    prev_color = None
    for info in order:
        prev_lst = change_elements(prev_lst,prev_color,info[0],info[1])
        prev_color = info[0]
        if init_color == None:
            init_color = info[0]
            continue

def change_TRUL_state(TRUL_state,color,dir):
    tmp_ki_lst = deque()
    for ki in TRUL_state[color].keys():
        tmp_ki_lst.append(TRUL_state[color][ki])
    if dir == '+':
        tmp_ki_lst.appendleft(tmp_ki_lst.pop())
    else:
        tmp_ki_lst.append(tmp_ki_lst.popleft())
    for ki in TRUL_state[color].keys():
        TRUL_state[color][ki] = tmp_ki_lst.popleft()
    return TRUL_state

t = int(input())
for i in range(t):
    TRUL_state = {'W':{'T':'T','R':'R','U':'U','L':'L'},
                  'R':{'T':'T','R':'R','U':'U','L':'L'},
                  'G':{'T':'T','R':'R','U':'U','L':'L'},
                  'B':{'T':'T','R':'R','U':'U','L':'L'},
                  'O':{'T':'T','R':'R','U':'U','L':'L'},
                  'Y':{'T':'T','R':'R','U':'U','L':'L'},}

    cube = {'W':[['w']*3 for i in range(3)],
            'R':[['r']*3 for i in range(3)],
            'G':[['g']*3 for i in range(3)],
            'B':[['b']*3 for i in range(3)],
            'O':[['o']*3 for i in range(3)],
            'Y':[['y']*3 for i in range(3)],}

    move_time = int(input())
    move_lst = list(input().split())
    for move in move_lst:
        color = face_2_color[move[0]]
        dir = move[1]
        spin_face(color,dir)
        spin_adj_faces(color,dir)

    for line in cube['W']:
        print(''.join(line))