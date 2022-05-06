from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

lst = [i for i in range(1,n+1)]

lst = deque(lst)
print('<',end="")
while(lst):
    for i in range(k-1):
        lst.append(lst.popleft())
    print(lst.popleft(),end="")
    if lst:
        print(', ',end="")
    else:
        print('>')
