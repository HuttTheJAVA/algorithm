from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(input().strip()))

visit = [[0]*m for i in range(n)]

group_matrix = [[0]*m for i in range(n)]

group_num = 1

dir_dct = {"D":1,"R":0,"L":2,"U":3}
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    for j in range(m):
        if not visit[i][j]: # 아직 방문되지 않았으니 그룹도 미지정이다.
            members = []
            qu = deque()
            qu.append((i,j))
            members.append((i,j))
            visit[i][j] = 1
            while(qu):
                x,y = qu.popleft()
                nx = x + dx[dir_dct[matrix[x][y]]]
                ny = y + dy[dir_dct[matrix[x][y]]]
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    qu.append((nx,ny))
                    members.append((nx,ny))
                else:
                    if group_matrix[nx][ny]:
                        for mem in members:
                            group_matrix[mem[0]][mem[1]] = group_matrix[nx][ny]
                        qu = []
                        members = []
                        continue
            if members:
                for mem in members:
                    group_matrix[mem[0]][mem[1]] = group_num
                group_num += 1

safe_zone = 0

for i in range(n):
    for j in range(m):
        safe_zone = max(safe_zone,group_matrix[i][j])

print(safe_zone)