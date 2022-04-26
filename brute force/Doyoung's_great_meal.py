import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

ingred = []

for i in range(n):
    s,b = map(int,input().split())
    ingred.append((s,b))

combi = []
minchai = 1000000001
for i in range(1,n+1):
    combi = list(combinations(ingred,i))
    for j in range(len(combi)):
        sour = 1
        bitter = 0
        for k in range(len(combi[j])):
            sour *= combi[j][k][0]
            bitter += combi[j][k][1]
        result = abs(sour-bitter)
        minchai = min(minchai,result)

print(minchai)