import sys
import copy
input = sys.stdin.readline

h,w = map(int,input().split())

block_heights = list(map(int,input().split()))

right_highest = copy.deepcopy(block_heights)    # 이 둘의 리스트는 좌측 기준과 우측 기준으로 자기보다 높은 블록이 있으면 최신화 될 것이고,
left_highest = copy.deepcopy(block_heights)     # 없으면 자기자신 그대로 유지 -> 해당 부분은 빗물이 0이 라는 소리.

highest = right_highest[0]

for i in range(1,len(right_highest)):
    if right_highest[i] < highest:
        right_highest[i] = highest
    else:
        highest = right_highest[i]

highest = left_highest[-1]

for i in range(len(left_highest)-2,-1,-1):
    if left_highest[i] < highest:
        left_highest[i] = highest
    else:
        highest = left_highest[i]

final_highest = [0]*len(right_highest)

for i in range(len(final_highest)):
    final_highest[i] = min(right_highest[i],left_highest[i])

water = 0

for i in range(len(right_highest)):
    water += final_highest[i] - block_heights[i]

print(water)