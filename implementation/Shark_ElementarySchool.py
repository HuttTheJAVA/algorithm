import sys
input = sys.stdin.readline

n = int(input())

my_friend_list = [0]*n**2

dx = [0,1,0,-1]
dy = [1,0,-1,0]

student_order = []

for i in range(n**2):
    lst = list(map(int,input().split()))
    my_friend_list[lst[0]-1] = lst[1:]
    student_order.append(lst[0]-1)  # 인덱스 0 맞춤

student_coordinate = ['empty']*n**2

is_preemptive_dct = {}

matrix = [[[0,0] for i in range(n)] for i in range(n)] # matrix[x][y][z] 3차원 행렬 형식

for i in range(n):
    for j in range(n):
        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if 0<=nx<n and 0<=ny<n:   ## 초기 상태니까 인접 칸이 찼는지 확인할 필요 x 단, 나중에 해당칸이 차면 그 인접 칸들의 비어있는 칸 수를 -= 1 해줘야함.
                matrix[i][j][1] += 1 

for student in student_order:
    for friend in my_friend_list[student]:
        friend_idx = friend - 1
        if student_coordinate[friend_idx] != 'empty':
            x = student_coordinate[friend_idx][0]
            y = student_coordinate[friend_idx][1]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<n and (nx,ny) not in is_preemptive_dct:
                    matrix[nx][ny][0] += 1
    my_x = None
    my_y = None
    adj_friends = None
    empty_cnt = None
    for i in range(n):
        for j in range(n):
            if (i,j) not in is_preemptive_dct:
                if my_x == None:
                    my_x = i
                    my_y = j
                    adj_friends = matrix[i][j][0]
                    empty_cnt = matrix[i][j][1]
                elif adj_friends < matrix[i][j][0]:
                    my_x = i
                    my_y = j
                    adj_friends = matrix[i][j][0]
                    empty_cnt = matrix[i][j][1]
                elif adj_friends == matrix[i][j][0] and empty_cnt < matrix[i][j][1]:
                    my_x = i
                    my_y = j
                    adj_friends = matrix[i][j][0]
                    empty_cnt = matrix[i][j][1]
    student_coordinate[student] = [my_x,my_y]
    is_preemptive_dct[(my_x,my_y)] = student # 인덱스 0에 맞춘 학생번호
    for i in range(n):
        for j in range(n):
            matrix[i][j][0] = 0
    
    for i in range(4):
        nx = my_x + dx[i]
        ny = my_y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            matrix[nx][ny][1] -= 1

satisfy_degree = 0

for i in range(n):
    for j in range(n):
        satisfy = 0
        student_idx = is_preemptive_dct[(i,j)]
        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            if 0<=nx<n and 0<=ny<n:
                adj_student = is_preemptive_dct[(nx,ny)] + 1
                if adj_student in my_friend_list[student_idx]:
                    satisfy += 1
        if satisfy == 1:
            satisfy_degree += 1
        elif satisfy == 2:
            satisfy_degree += 10
        elif satisfy == 3:
            satisfy_degree += 100
        elif satisfy == 4:
            satisfy_degree += 1000

print(satisfy_degree)
