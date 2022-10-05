import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

stack = [lst[-1]]

accumulate = [-1]

for i in range(len(lst)-2,-1,-1):
    while(stack):
        if lst[i]>=stack[-1]:
            stack.pop()
        else:
            break
    if stack:
        accumulate.append(stack[-1])
    else:
        accumulate.append(-1)
    stack.append(lst[i])

accumulate = accumulate[::-1]

print(*accumulate)