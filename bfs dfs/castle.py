from collections import deque
import sys

input = sys.stdin.readline

def make_binary_lst(val):
    dir_lst = [0,0,0,0,0] # 동,남,서,북,그룹 아이덴티티
    if val >= 2**3:
        dir_lst[1] = 1
        val -= 2**3
    if val >= 2**2:
        dir_lst[0] = 1
        val -= 2**2
    if val >= 2:
        dir_lst[3] = 1
        val -= 2
    if val >= 1:
        dir_lst[2] = 1
        val -= 1
    
    return dir_lst

dx = [0,1,0,-1]
dy = [1,0,-1,0]

n,m = map(int,input().split())

matrix = []
                                            #cnt,related_group
dct_of_group_cnt_n_related_group = {} ### ==> [0,set()]

for i in range(m):
    matrix.append(list(map(int,input().split())))

# matrix의 한개 좌표 값을 4방향의 리스트 및 영역 정보의 값으로 바꾼다.

visit = [[0]*n for i in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = make_binary_lst(matrix[i][j])

group_number = 1
## 이 아래 코드도 for문 안에서 짜주자

for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            qu = deque()
            qu.append((i,j))
            matrix[i][j][4] = group_number
            dct_of_group_cnt_n_related_group[group_number] = [1,set()]
            visit[i][j] = 1

            ## 전체 순회 for문 짜주야함 지금 코드는 하나의 그룹만 만들어주기 때문에
            while(qu):
                x,y = qu.popleft()
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if 0<=nx<m and 0<=ny<n:
                        if not matrix[x][y][idx]:
                            if not visit[nx][ny]:
                                dct_of_group_cnt_n_related_group[matrix[x][y][4]][0] += 1
                                visit[nx][ny] = 1
                                matrix[nx][ny][4] = matrix[x][y][4]
                                qu.append((nx,ny))
                        else:
                            ## visit 이여도 다른그룹확인은 해줘야함.
                            if matrix[nx][ny][4] != 0 and matrix[x][y][4] != matrix[nx][ny][4]:
                                dct_of_group_cnt_n_related_group[matrix[x][y][4]][1].add(matrix[nx][ny][4])
            group_number+=1

group_cnt = 0
max_group_cnt = 0
max_break_wall_group = 0
group_cnt = max(group_cnt,len(dct_of_group_cnt_n_related_group))
for group in dct_of_group_cnt_n_related_group.keys():
    max_group_cnt = max(max_group_cnt,dct_of_group_cnt_n_related_group[group][0])
    for relate_group in dct_of_group_cnt_n_related_group[group][1]:
        max_break_wall_group = max(max_break_wall_group,dct_of_group_cnt_n_related_group[group][0]+dct_of_group_cnt_n_related_group[relate_group][0])

print(group_cnt)
print(max_group_cnt)
print(max_break_wall_group)
