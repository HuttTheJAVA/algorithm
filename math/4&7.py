from collections import deque
import sys

k = int(input())

stack = 0

lst = [0,0]

for i in range(1,10000000):
    stack += 2**i
    lst.append(stack)
    if stack >= 1000_000_000:
        break

res = ''

is_made = False

leng = 0

for i in range(len(lst)-1,-1,-1):
    if k==lst[i]:
        res = '7'*(i-1)
        is_made = True
        break
    elif k>lst[i]:
        leng = i
        k -= lst[i]
        break

if not is_made:
    for i in range(leng):
        if k>2**((leng-1)-i):
            res = res + '7'
            k -= 2**((leng-1)-i)
        else:
            res = res + '4'

print(res)