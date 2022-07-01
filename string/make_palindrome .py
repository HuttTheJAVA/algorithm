from collections import deque
import sys
input = sys.stdin.readline

name = input().strip()

left = 0
is_middle = ""
idx = 0
lst = [0]*(ord('Z')-ord('A')+1)
res = True
Palindrome_l = ""
Palindrome_R = ""

for i in range(len(name)):
    lst[ord(name[i])-65] += 1
    left += 1

while(idx<len(lst)):
    if lst[idx]:
        if lst[idx] == 1:
            if is_middle == "":
                is_middle = chr(65+idx)
                lst[idx] -= 1
            else:
                res = False
                break
        else:
            portion = lst[idx]//2
            Palindrome_l += chr(65+idx)*portion
            Palindrome_R += chr(65+idx)*portion
            lst[idx] -= portion*2
    if not lst[idx]:
        idx += 1

if res:
    if is_middle:
        print(Palindrome_l+is_middle+Palindrome_R[::-1])
    else:
        print(Palindrome_l+Palindrome_R[::-1])
else:
    print("I'm Sorry Hansoo")