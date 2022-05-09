import sys
input = sys.stdin.readline
n = int(input())

nums = list(map(int,input().split()))

plus,minus,times,div = map(int,input().split())

min_val = 1000000000
max_val = -1000000000

def calculate(plus,minus,times,div,val,idx):
    global min_val
    global max_val
    if not sum([plus,minus,times,div]):
        min_val = min(min_val,val)
        max_val = max(max_val,val)
        return
    for i in range(idx+1,len(nums)):
        if plus:
            calculate(plus-1,minus,times,div,val+nums[i],i)
        if minus:
            calculate(plus,minus-1,times,div,val-nums[i],i)
        if times:
            calculate(plus,minus,times-1,div,val*nums[i],i)
        if div:
            if val<0:
                new_val = abs(val)//nums[i]
                new_val = -new_val
            else:
                new_val = val//nums[i]
            calculate(plus,minus,times,div-1,new_val,i)

for i in range(len(nums)):
    calculate(plus,minus,times,div,nums[i],i)

print(max_val)
print(min_val)