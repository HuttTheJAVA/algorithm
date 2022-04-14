from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

data = []

for _ in range(N):
    data.append(list(map(int,input().strip())))


def cut(lst,N):

    if N == 1:
        print(lst[0][0],end="")
        return

    hab = 0

    for lines in lst:
        hab += sum(lines)
    
    if hab == 0:
        print("0",end="")
        return
    elif hab == N**2:
        print("1",end="")
        return
    print("(",end="")
    g1 = [lst[i][0:N//2] for i in range(N//2)]
    g2 = [lst[i][N//2:] for i in range(N//2)]
    g3 = [lst[i][0:N//2] for i in range(N//2,N)]
    g4 = [lst[i][N//2:] for i in range(N//2,N)]

    cut(g1,N//2)
    cut(g2,N//2)
    cut(g3,N//2)
    cut(g4,N//2)
    print(")",end="")
    return

cut(data,N)