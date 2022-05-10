import sys
input = sys.stdin.readline

n,m = map(int,input().split())

nums = [i for i in range(1,n+1)]

def back(lst):
    if len(lst) == m:
        for i in lst:
            print(i,end=" ")
        print()
        return
        
    for j in range(len(nums)):
        lst.append(nums[j])
        val = nums[j]
        nums.pop(j)
        
        back(lst)
        lst.pop()
        nums.insert(j,val)

back([])