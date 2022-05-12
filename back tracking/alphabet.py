import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(input().strip()))

max_leng = 0

alp_done = [0]*(ord('Z')-ord('A')+1)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def make_alpha_route(alp_done,x,y,cnt):
    global max_leng
    global dx
    global dy
    global matrix
    res = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if not alp_done[ord(matrix[nx][ny])-65]:
                alp_done[ord(matrix[nx][ny])-65] = 1
                res = False
                make_alpha_route(alp_done,nx,ny,cnt+1)
                alp_done[ord(matrix[nx][ny])-65] = 0
    if res:
        max_leng = max(max_leng,cnt)
        return

alp_done[ord(matrix[0][0])-65] = 1
make_alpha_route(alp_done,0,0,1)

print(max_leng)