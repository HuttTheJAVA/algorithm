from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dice = list(map(int,input().split()))

max_dice_num = max(dice)

min_dice_num = min(dice)

three_face = {0:[(2,4),(1,2),(1,3),(3,4)],1:[(0,3),(0,2),(2,5),(3,5)],2:[(0,4),(0,1),(1,5),(4,5)],3:[(0,4),(0,1),(1,5),(4,5)],4:[(0,2),(0,3),(3,5),(2,5)],5:[(1,2),(1,3),(3,4),(2,4)]}

two_face = {0:[1,2,3,4],1:[0,2,3,5],2:[0,1,4,5],3:[0,1,4,5],4:[0,2,3,5],5:[1,2,3,4]}

total = None

if n == 1:
    total = sum(dice)-max_dice_num
else:
    min_three_face = max_dice_num*3
    min_two_face = max_dice_num*2
    for k in three_face.keys():
        val = dice[k]
        for idx in three_face[k]:
            adj_sum = 0
            for adj in idx:
                adj_sum += dice[adj]
            if val+adj_sum < min_three_face:
                min_three_face = val+adj_sum
    
    for k in two_face.keys():
        val = dice[k]
        for adj in two_face[k]:
            if val+dice[adj] < min_two_face:
                min_two_face = val+dice[adj]
    one_cnt = 5*(n-2)**2+4*(n-2)
    two_cnt = 4*(n-2)+4*(n-1)
    three_cnt = 4

    total = one_cnt*min_dice_num + two_cnt*min_two_face + three_cnt *min_three_face

print(total)
