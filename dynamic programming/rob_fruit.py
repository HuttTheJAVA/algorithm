import sys
input = sys.stdin.readline

kind = int(input())

steal_gwak = int(input())

combi = [[0]*(steal_gwak+1) for i in range(31)]

for i in range(1,steal_gwak+1):
    combi[1][i] = 1

for i in range(2,kind+1):
    for j in range(i,steal_gwak+1):
        combi[i][j] = combi[i][j-1] + combi[i-1][j-1]

print(combi[kind][steal_gwak])