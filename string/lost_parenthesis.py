import sys
from collections import deque

input = sys.stdin.readline

word = input().strip()
calcs = deque()
nums = deque()
new_word = ''
for i in range(len(word)):
    if word[i] == '-' or word[i] == '+':
        calcs.append(word[i])
        if new_word:
            nums.append(new_word)
            new_word = ''
    else:
        if not len(new_word) and word[i] == '0':
            continue
        else:
            new_word += word[i]

if new_word:
    nums.append(new_word)

cal = int(nums.popleft())

on = False

hab = 0

while(nums):
    plus_minus = calcs.popleft()
    number = int(nums.popleft())
    if on and plus_minus == '-':
        cal -= hab
        hab = number
    elif not on and plus_minus =='-':
        on = True
        hab = number
    elif on and plus_minus == '+':
        hab += number
    else:
        cal += number

if hab != 0:
    cal -= hab

print(cal)