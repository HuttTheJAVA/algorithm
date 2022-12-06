import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))

start = 0
end = n-1

min_sum = 123321321313213132312321313213

res = []

while(start<end):
    hab = lst[start] + lst[end]
    if abs(hab)<min_sum:
        res = [lst[start],lst[end]]
        min_sum = abs(hab)
        if not hab:
            break
    if hab > 0:
        end -= 1
    else:
        start += 1

print(*res)