import sys
input = sys.stdin.readline

n = int(input())

G_M_T_P = 0

for i in range(1,n):
    G_M_T_P += i

print(G_M_T_P)