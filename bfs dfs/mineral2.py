from collections import deque
import sys

input = sys.stdin.readline

r,c = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(r):
    lst = list(input().strip())
    matrix.append(lst)

n = int(input())

throw = list(map(int,input().split()))

for idx in range(n):
    x = r - throw[idx]
    crash = False
    if not idx%2:
        y = 0
        dyy = 1             # 위의 dy리스트 하고 겹쳐서 이렇게 명시
    else:
        y = c-1
        dyy = -1
    while(1):
        if 0<=x<r and 0<=y<c:
            if matrix[x][y] == 'x':
                matrix[x][y] = '.'
                crash = True
                break
            else:
                y += dyy
        else:
            break
    if not crash:
        continue
    visit = [[0]*c for i in range(r)]
    gravity_need_clusters = None
    on_ground = True
    for i in range(r-2,-1,-1):     # 바닥서 부터 탐색해야함.
        for j in range(c):
            if matrix[i][j] == 'x' and not visit[i][j]:
                cluster_lst = [[i,j]]
                on_ground = False # i는 밑에서 2번 째 부터 탐색하므로,시작부터 on_ground 일 수가 없음
                qu = deque()
                qu.append([i,j])
                visit[i][j] = 1
                while(qu):
                    x,y = qu.popleft()
                    if x == r-1:
                        on_ground = True
                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        if 0<=nx<r and 0<=ny<c and not visit[nx][ny] and matrix[nx][ny] == 'x':
                            qu.append([nx,ny])
                            cluster_lst.append([nx,ny])
                            visit[nx][ny] = 1
                if not on_ground: # 클러스터 2개가 동시에 떨어지는 일은 없댔으니까, 땅에 닿지않은 클러스터가 발생 시 곧바로 2중 for문을 빠져나온다.
                    break
            if not on_ground:
                break
        if not on_ground:
            break
    if on_ground: # 공중에 있는 클러스터가 없으면 중력 작용 시킬 필요없음.
        continue
    gravity_need_clusters = cluster_lst # cluster_lst가 빈 리스트 일 수가 없음 (50번줄)
    # 참고로 자기 자신의 아랫 방향(4 방향 아님)이 r이거나 공중 클러스터에 속하지 않은 미네랄이 있으면 중력을 더 이상 작용 시키지 않는다.
    
    for x_y in gravity_need_clusters:
        matrix[x_y[0]][x_y[1]] = 'xx' # 나중에 중력 작용 시키고 마지막에 x로 다시 바꿔 줘야함. 중력 작용시키면 더 이상 공중 클러스터가 아니므로

    not_contact = True
    gravity_need_clusters.sort(key=lambda x:(-x[0],x[1])) # 가장 아래 있는 애들부터 앞으로 오게 아래부터 한칸씩 땡겨야 겹치지 않게 마킹됨. 
    while(not_contact):

        for i in range(len(gravity_need_clusters)):
            matrix[gravity_need_clusters[i][0]][gravity_need_clusters[i][1]] = '.'
            gravity_need_clusters[i][0] += dx[1]
            matrix[gravity_need_clusters[i][0]][gravity_need_clusters[i][1]] = 'xx'
        for i in range(len(gravity_need_clusters)):
            if gravity_need_clusters[i][0]+dx[1] == r or 0<=gravity_need_clusters[i][0]+dx[1]<r and matrix[gravity_need_clusters[i][0]+dx[1]][gravity_need_clusters[i][1]] == 'x':
                not_contact = False
                break
    
    for x_y in gravity_need_clusters:
        matrix[x_y[0]][x_y[1]] = 'x'

for i in range(r):
    for j in range(c):
        print(matrix[i][j],end="")
    print()