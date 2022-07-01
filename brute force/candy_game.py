import sys
input = sys.stdin.readline

n = int(input())

matrix = []

dx = [0,1]
dy = [1,0]

for i in range(n):
    matrix.append(list(input().strip()))
max_len = 0
for i in range(n):
    for j in range(n):
        for k in range(2):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                temp1 = matrix[i][j]
                temp2 = matrix[nx][ny]
                matrix[i][j] = temp2
                matrix[nx][ny] = temp1
            else:
                continue
            word = ''
            word2 = ''
            word3 = ''
            for l in range(n):
                if word == '':
                    word += matrix[i][l]
                else:
                    if word[-1] == matrix[i][l]:
                        word += matrix[i][l]
                        if len(word) == 5:
                            print
                    else:
                        max_len = max(max_len,len(word))
                        word = matrix[i][l]

                if word2 == '':
                    word2 += matrix[l][j]
                else:
                    if word2[-1] == matrix[l][j]:
                        word2 += matrix[l][j]
                    else:
                        max_len = max(max_len,len(word2))
                        word2 = matrix[l][j]
                if k:
                    if word3 == '':
                        word3 += matrix[nx][l]
                    else:
                        if word3[-1] == matrix[nx][l]:
                            word3 += matrix[nx][l]
                        else:
                            max_len = max(max_len,len(word3))
                            word3 = matrix[nx][l]
                else:
                    if word3 == '':
                        word3 += matrix[l][ny]
                    else:
                        if word3[-1] == matrix[l][ny]:
                            word3 += matrix[l][ny]
                        else:
                            max_len = max(max_len,len(word3))
                            word3 = matrix[l][ny]

            max_len = max(len(word),len(word2),len(word3),max_len)
            
            matrix[i][j] = temp1
            matrix[nx][ny] = temp2

print(max_len)