from collections import deque
import sys
input = sys.stdin.readline

word = input().strip()

p_cnt = 0
p_pass = 0
res = True
for i in range(len(word)):
    if word[i] == 'P':
        if not p_pass:
            p_cnt += 1
        else:
            p_pass = 0
    else:
        if p_cnt > 1:
            if i+1<len(word) and word[i+1] == 'P':
                p_pass = 1
                p_cnt -= 1
            else:
                res = False
                break
        else:
            res = False
            break

if res and p_cnt == 1:
    print("PPAP")
else:
    print("NP")