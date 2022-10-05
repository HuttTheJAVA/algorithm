import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

matrix = []

team_bit = [0]*n

people = [i for i in range(n)]

min_gap = 101*21*21*21

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

combi_lst = []

for combi in combinations(people,n//2):
    combi_lst.append(combi)

for combi in combi_lst:

    team1 = 0
    team2 = 0

    for member in combi:
        team_bit[member] = 1
    
    for i in range(n):
        for j in range(n):
            if not team_bit[i] and not team_bit[j]:
                team1 += matrix[i][j]
            elif team_bit[i] and team_bit[j]:
                team2 += matrix[i][j]
    
    for member in combi:
        team_bit[member] = 0

    min_gap = min(min_gap,abs(team1 - team2))

print(min_gap)