from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    leng = int(input())
    alp_lst = list(input().split())
    word = alp_lst[0]
    for j in range(1,len(alp_lst)):
        if ord(alp_lst[j])<=ord(word[0]):
            word = alp_lst[j]+word
        else:
            word = word+alp_lst[j]

    print(word)