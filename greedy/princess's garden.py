import sys

input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    a,b,c,d = map(int,input().split())
    lst.append((a,b,c,d))

lst.sort(key=lambda x:(x[0],x[1],-x[2],-x[3]))

stack = []

for i in range(len(lst)):
    if not stack:
        if lst[i][0] < 3 or lst[i][0] == 3 and lst[i][1] == 1:
            stack.append((lst[i][0],lst[i][1],lst[i][2],lst[i][3],3,1)) # 시작 달,시작 일,끝 달,끝 일,그 전 끝 달,그 전 끝 일

    else:
        while(stack):
            if (lst[i][0] < stack[-1][4] or lst[i][0] == stack[-1][4] and lst[i][1] <= stack[-1][5]) and (lst[i][2] > stack[-1][2] or lst[i][2] == stack[-1][2] and lst[i][3] > stack[-1][3]):
                stack.pop()
            else:
                if stack[-1][2] > 11:
                    break
                if (lst[i][0]<stack[-1][2] or lst[i][0] == stack[-1][2] and lst[i][1] <= stack[-1][3]) and (lst[i][2]>stack[-1][2] or lst[i][2] == stack[-1][2] and lst[i][3] > stack[-1][3]):
                    stack.append((lst[i][0],lst[i][1],lst[i][2],lst[i][3],stack[-1][2],stack[-1][3]))
                break
        if not stack:
            if lst[i][0] < 3 or lst[i][0] == 3 and lst[i][1] == 1:
                stack.append((lst[i][0],lst[i][1],lst[i][2],lst[i][3],3,1))
    
if stack and stack[-1][2] > 11:
    print(len(stack))
else:
    print(0)