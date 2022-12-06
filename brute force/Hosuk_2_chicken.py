import sys
input = sys.stdin.readline
from itertools import combinations
n,m = map(int,input().split())

edge = []

dist_matrix = [[sys.maxsize]*(n) for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    dist_matrix[a-1][b-1] = 1
    dist_matrix[b-1][a-1] = 1

num = [i for i in range(n)]

for i in range(n):
    dist_matrix[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist_matrix[j][i] + dist_matrix[i][k] < dist_matrix[j][k]:
                dist_matrix[j][k] = dist_matrix[j][i] + dist_matrix[i][k]

min_dist = sys.maxsize

city = None

for combi in combinations(num,2):
    sum_dist = 0
    a = combi[0]
    b = combi[1]
    for i in range(n):
        sum_dist += min(dist_matrix[i][a]*2,dist_matrix[i][b]*2)
    if sum_dist<min_dist:
        city = [combi[0]+1,combi[1]+1]
        min_dist = sum_dist

print(*city,min_dist)