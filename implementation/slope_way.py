import sys

input = sys.stdin.readline

n,l = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

road = 0

for j in range(n):   # ↓ ->
    cnt = 0
    prev = matrix[0][j]
    reach = True
    decline_mode = 0
    for i in range(n):
        if decline_mode:
            if matrix[i][j] == prev:
                cnt += 1
                if cnt == l:
                    decline_mode = 0
                    cnt = 0
            else:
                reach = False
                break
            
        elif matrix[i][j] == prev:
            cnt += 1
        else:
            if matrix[i][j] == prev + 1 and cnt >= l:
                cnt = 1
                prev = matrix[i][j]
            elif matrix[i][j]+1 == prev:
                decline_mode = 1
                cnt = 1
                prev = matrix[i][j]
                if cnt == l:
                    decline_mode = 0
                    cnt = 0
            else:
                reach = False
                break
    if decline_mode:
        if cnt<l:
            reach = False
    if reach:
        road += 1

for i in range(n):   # -> ↓
    cnt = 0
    prev = matrix[i][0]
    reach = True
    decline_mode = 0
    for j in range(n):
        if decline_mode:
            if matrix[i][j] == prev:
                cnt += 1
                if cnt == l:
                    decline_mode = 0
                    cnt = 0
            else:
                reach = False
                break
        elif matrix[i][j] == prev:
            cnt += 1
        else:
            if matrix[i][j] == prev + 1 and cnt >= l:
                cnt = 1
                prev = matrix[i][j]
            elif matrix[i][j]+1 == prev:
                decline_mode = 1
                cnt = 1
                prev = matrix[i][j]
                if cnt == l:
                    decline_mode = 0
                    cnt = 0
            else:
                reach = False
                break
    if decline_mode:
        if cnt<l:
            reach = False
    if reach:
        road += 1

print(road)