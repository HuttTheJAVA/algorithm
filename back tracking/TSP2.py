import sys
input = sys.stdin.readline

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

visit = [0]*n

min_cost = sys.maxsize

def travel_next_city(cost,now_city,init_city,visit_cnt):
    global visit
    global min_cost
    global n
    if visit_cnt == n:
        if matrix[now_city][init_city]:
            min_cost = min(min_cost,cost+matrix[now_city][init_city])
            return
    if cost>=min_cost:
        return
    for i in range(len(visit)):        
        if not visit[i] and matrix[now_city][i]:
            visit[i] = 1
            travel_next_city(cost+matrix[now_city][i],i,init_city,visit_cnt+1)
            visit[i] = 0

for i in range(len(matrix)):
    visit[i] = 1
    travel_next_city(0,i,i,1)
    visit[i] = 0

print(min_cost)
