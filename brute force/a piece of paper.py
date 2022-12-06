import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,list(input().strip()))))

assign_matrix = [[0]*m for i in range(n)]
max_hab = 0
def recursive_search(start_i,hab,assign_cnt):
    global assign_matrix,n,m,max_hab
    if assign_cnt == n*m:
        max_hab = max(max_hab,hab)
        return
    found = False
    for i in range(start_i,n):
        for j in range(m):
            if not assign_matrix[i][j]: # 다음 봐야될 좌표가 이미 할당 상태이면,그 쪽으로는 더이상 진행 불가임.
                found = True
                num = ''
                x_y_coor = []
                for right in range(m-j):
                    if not assign_matrix[i][j+right]:
                        assign_matrix[i][j+right] = 1
                        num += str(matrix[i][j+right])
                        x_y_coor.append((i,j+right))
                        recursive_search(i,hab+int(num),assign_cnt+(right+1))
                    else:
                        break

                while(x_y_coor):
                    x,y = x_y_coor.pop()
                    assign_matrix[x][y] = 0

                num = ''
                for under in range(n-i):
                    if not assign_matrix[i+under][j]:
                        assign_matrix[i+under][j] = 1
                        num += str(matrix[i+under][j])
                        x_y_coor.append((i+under,j))
                        recursive_search(i,hab+int(num),assign_cnt+(under+1))
                    else:
                        break

                while(x_y_coor):
                    x,y = x_y_coor.pop()
                    assign_matrix[x][y] = 0
            if found:
                break
        if found:
            break
recursive_search(0,0,0)
print(max_hab)