from collections import deque
import sys
input = sys.stdin.readline

n,M,k = map(int,input().split())

matrix = []

after_move_matrix = []

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

matrix = [[deque() for i in range(n)] for i in range(n)]

after_move_matrix = [[deque() for i in range(n)] for i in range(n)]

qu = deque()

for i in range(M):
    r,c,m,s,d = map(int,input().split())
    matrix[r-1][c-1].append((m,s,d))
    qu.append((r-1,c-1))

for _ in range(k):
    cash_s = [[0]*n for i in range(n)]
    cash_m = [[0]*n for i in range(n)]
    odd_even_cnt = [[[0,0] for i in range(n)] for i in range(n)]
    while(qu):
        x,y = qu.popleft()
        m,s,d = matrix[x][y].popleft()
        nx = ((x+dx[d]*s)%n + n) % n
        ny = ((y+dy[d]*s)%n + n) % n
        after_move_matrix[nx][ny].append((m,s,d))
        odd_even_cnt[nx][ny][d%2] += 1
        cash_m[nx][ny] += m
        cash_s[nx][ny] += s
    
    for i in range(n):
        for j in range(n):
            leng = len(after_move_matrix[i][j])
            if leng>=2:
                after_move_matrix[i][j] = deque()
                if cash_m[i][j]//5:
                    new_m = cash_m[i][j]//5
                    new_s = cash_s[i][j]//leng
                    if not odd_even_cnt[i][j][0] or odd_even_cnt[i][j][0] == leng:
                        for n_dir in range(0,7,2):
                            after_move_matrix[i][j].append((new_m,new_s,n_dir))
                    else:
                        for n_dir in range(1,8,2):
                            after_move_matrix[i][j].append((new_m,new_s,n_dir))

    matrix = after_move_matrix

    for i in range(n):
        for j in range(n):
            if len(matrix[i][j]):
                for k in range(len(matrix[i][j])):
                    qu.append((i,j))
    sum_m = 0

    for i in range(n):
        for j in range(n):
            if len(matrix[i][j]):
                for k in range(len(matrix[i][j])):
                    sum_m += matrix[i][j][k][0]
    
print(sum_m)