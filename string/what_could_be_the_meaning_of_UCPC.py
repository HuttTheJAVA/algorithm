from collections import deque
import sys
input = sys.stdin.readline

word = input().strip()
ch = [0,0,0,0]

for alp in word:
    if alp == 'U':
        ch[0]=1
    if alp=='C' and ch[0]:
        ch[1]=1
    if alp=='P' and ch[1]:
        ch[2]=1
    if alp=='C' and ch[2]:
        ch[3]=1

if not ch.count(0):
    print("I love UCPC")
else:
    print("I hate UCPC")