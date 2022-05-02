import sys
from itertools import combinations
input = sys.stdin.readline


while(1):
    lotto = list(map(int,input().split()))
    if len(lotto)==1 and sum(lotto) == 0:
        break
    for vals in combinations(lotto[1:],6):
        for nums in vals:
            print(nums,end=" ")
        print()
    print()