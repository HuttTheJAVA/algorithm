from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

chicken_lst = []
cnt = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            chicken_lst.append([i,j])
            cnt += 1
home_lst = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            dist_lst = []
            for chicken in chicken_lst:
                dist = abs(i-chicken[0]) + abs(j-chicken[1])
                dist_lst.append(dist)
            home_lst.append(dist_lst)

chicken_num = [i for i in range(cnt)]

result_dist_sum = sys.maxsize

for num_set in combinations(chicken_num,m):
    min_dist_sum = 0
    for i in range(len(home_lst)):   # 하나의 개별집에 대해
        min_house_dist = sys.maxsize
        for num in num_set: # 각 치킨집마다 최단거리를 구해서
            min_house_dist = min(min_house_dist,home_lst[i][num])
        min_dist_sum += min_house_dist
    result_dist_sum = min(result_dist_sum,min_dist_sum)

print(result_dist_sum)
