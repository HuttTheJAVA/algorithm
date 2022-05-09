import sys

input = sys.stdin.readline

N,M = map(int,input().split())
rainz = max(N,M)
data = [[0]*1001 for i in range(1001)]
for i in range(len(data)-1):
    data[0][i] = 1
    data[i][0] = 1

for i in range(1,N):
    for j in range(1,M):
        data[i][j] = data[i-1][j]%1000000007+data[i-1][j-1]%1000000007+data[i][j-1]%1000000007

print(data[N-1][M-1]%1000000007)