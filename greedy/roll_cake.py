from collections import deque
import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())

heap = []

lst = list(map(int,input().split()))

cnt = 0

for roll in lst:
    if roll > 10:
        heapq.heappush(heap,(roll%10,roll))
    elif roll == 10:
        cnt += 1


while(heap and m):
    rest,roll = heapq.heappop(heap)
    if not rest:
        if roll//10 - 1 <= m:
            m -= roll//10 - 1
            cnt += roll//10
        else:
            cnt += m
            m -= m      # 어차피 m은 여기서 0이 되므로(= while break) heap에 다시 넣는다던가 자르고 남은 left를 고려할 필요가 없음.
    else:
        cut_time = min(roll//10,m)
        m -= cut_time
        cnt += cut_time
        left = roll - 10*cut_time
        if left>10:
            heapq.heappush(heap,(left%10,left))

print(cnt)

