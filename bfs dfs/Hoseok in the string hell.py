import sys

input = sys.stdin.readline

n,m,k = map(int,input().split())

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

matrix = []

for i in range(n):
    lst = list(input().strip())
    matrix.append(lst)

dct = {}
order_lst = []
for i in range(k):
    word = input().strip()
    dct[word] = 0
    order_lst.append(word)

def transfer_x_y(x,y):
    if x >= n:
        x = 0
    if x < 0:
        x = n-1
    if y >= m:
        y = 0
    if y < 0:
        y = m-1
    return x,y

def dfs(visit,word,x,y):
    if word in dct.keys():
        dct[word] += 1
    if len(word) >= 5:
        return
    
    for i in range(8):
        nx,ny = transfer_x_y(x + dx[i],y + dy[i])
        # if not visit[nx][ny]:
            # visit[nx][ny] = 1
        dfs(visit,word+matrix[nx][ny],nx,ny)
            # visit[nx][ny] = 0

visit = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        # visit[i][j] = 1
        dfs(visit,matrix[i][j],i,j)
        # visit[i][j] = 0

for god_word in order_lst:
    print(dct[god_word])