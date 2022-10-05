from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

matrix = [[0]*(n+1)]

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

for i in range(1,n+1):
    matrix[i] = [0]+matrix[i]

total_sum = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        total_sum += matrix[i][j]

min_gap = 100*20*20*20

def preempt_section5(d1,d2,x,y):
    global bfs_matrix
    set_1 = set()
    for i in range(d1+1):
        if 1<=x+i<=n and 1<=y-i<=n:
            set_1.add((x+i,y-i))
        if 1<=x+d2+i<=n and 1<=y+d2-i<=n:
            set_1.add((x+d2+i,y+d2-i))

    for i in range(d2+1):
        if 1<=x+i<=n and 1<=y+i<=n:
            set_1.add((x+i,y+i))
        if 1<=x+d1+i<=n and 1<=y-d1+i<=n:
            set_1.add((x+d1+i,y-d1+i))

    lst = list(set_1)
    lst.sort(key=lambda x:(x[0],x[1]))
    lst = deque(lst)
    return lst

for d1 in range(1,n+1):
    for d2 in range(1,n+1):
        for x in range(1,n+1):
            if 1<=x<x+d1+d2<=n:
                for y in range(1,n+1):
                    if 1<=y-d1<y<y+d2<=n:
                        section1 = 0
                        section2 = 0
                        section3 = 0
                        section4 = 0
                        section5 = 0
                        section_threshold_lst = preempt_section5(d1,d2,x,y)
                        bfs_matrix = [[0]*(n+1) for i in range(n+1)]
                        for ki in section_threshold_lst:
                            bfs_matrix[ki[0]][ki[1]] = 1
                            section5 += matrix[ki[0]][ki[1]]

                        section_threshold_lst.pop()
                        section_threshold_lst.popleft()

                        prev = section_threshold_lst.popleft()

                        while(section_threshold_lst):
                            now = section_threshold_lst.popleft()
                            if prev[0] == now[0]:
                                for i in range(prev[1]+1,now[1]):
                                    bfs_matrix[prev[0]][i] = 2
                            
                            prev = now

                        for i in range(1,n+1):
                            for j in range(1,n+1):
                                if bfs_matrix[i][j] == 1:
                                    continue
                                if bfs_matrix[i][j] == 2:
                                    section5 += matrix[i][j]
                                    continue
                                if 1<=i<x+d1 and 1<=j<=y:
                                    section1 += matrix[i][j]
                                elif 1<=i<=x+d2 and y<j<=n:
                                    section2 += matrix[i][j]
                                elif x+d1<=i<=n and 1<=j<y-d1+d2:
                                    section3 += matrix[i][j]
                                elif x+d2<i<=n and y-d1+d2<=j<=n:
                                    section4 += matrix[i][j]
                        if section1 and section2 and section3 and section4 and section5:
                            lst = [section1,section2,section3,section4,section5]
                            lst.sort()
                            min_gap = min(min_gap,lst[-1]-lst[0])

print(min_gap)