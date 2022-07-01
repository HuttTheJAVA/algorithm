from collections import deque
import sys
input = sys.stdin.readline

word = input().strip()

As = ""
Bs = ""
res = ''

for i in range(len(word)):
    if word[i] != '.':
        As += "A"
        Bs += "B"
        if len(As) == 4:
            res += As
            As = ""
            Bs = ""
            continue
    else:
        if len(As) == 4:
            res += As
            As = ""
            Bs = ""
            
        elif len(Bs) == 2:
            res += Bs
            As = ""
            Bs = ""
        elif len(As)%2 or len(Bs)%2:
            res = -1
            break
        res += '.'

if len(As) == 4:
    res += As
elif len(Bs) == 2:
    res += Bs
elif len(As)%2 or len(Bs) %2:
    res = -1

print(res)