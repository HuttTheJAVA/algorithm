from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

data = []

for _ in range(N):
    data.append(list(map(int,input().split())))

White_Blue = [0,0]

def cut(lst,N):
    global White_Blue

    if N == 1:
        White_Blue[lst[0][0]] += 1
        return

    paper = 0

    for line in lst:
        paper += sum(line)
    
    if paper==0:
        White_Blue[paper] += 1
        return
    
    elif paper==N**2:
        White_Blue[1] += 1
        return

    g1 = [lst[i][0:N//2] for i in range(N//2)]
    g2 = [lst[i][N//2:] for i in range(N//2)]
    g3 = [lst[i][0:N//2] for i in range(N//2,N)]
    g4 = [lst[i][N//2:] for i in range(N//2,N)]

    cut(g1,N//2)
    cut(g2,N//2)
    cut(g3,N//2)
    cut(g4,N//2)
    return

cut(data,N)
print(White_Blue[0])
print(White_Blue[1])