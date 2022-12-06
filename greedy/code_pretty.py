from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

origin_line = list(map(int,input().split()))

to_make_line = list(map(int,input().split()))

calc = 0

for i in range(n):
    gap = to_make_line[i] - origin_line[i]
    if gap:
        while(1):
            gap = to_make_line[i] - origin_line[i]
            if not gap:
                break
            group_line = [i]
            min_line = abs(gap)
            for j in range(i+1,n):
                adj_gap = to_make_line[j] - origin_line[j]
                if adj_gap and abs(gap*adj_gap) == gap*adj_gap:
                    min_line = min(min_line,abs(adj_gap))
                    group_line.append(j)
                else:
                    break
            if len(group_line) == 1:
                if gap > 0:
                    origin_line[i] += gap
                else:
                    origin_line[i] -= gap
                calc += abs(gap)
                break
            else:
                for idx in group_line:
                    if gap > 0:
                        origin_line[idx] += min_line
                    else:
                        origin_line[idx] -= min_line
                calc += min_line
print(calc)