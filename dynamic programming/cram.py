import sys

input = sys.stdin.readline

n,t = map(int,input().split())

knap = [[0]*(t+1) for i in range(n+1)]

score_table = [0]

time_table = [0]

for i in range(n):
    time,score = map(int,input().split())
    score_table.append(score)
    time_table.append(time)

for i in range(1,n+1): # 행 점수
    for j in range(1,t+1): # 열 시간
        if j>=time_table[i]:
            knap[i][j] = max(knap[i-1][j],knap[i-1][j-time_table[i]]+score_table[i],knap[i][j])
        else:
            knap[i][j] = max(knap[i][j],knap[i-1][j])

print(knap[n][t])