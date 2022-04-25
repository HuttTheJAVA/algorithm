import sys

input = sys.stdin.readline

k,n = map(int,input().split())

lst = list(map(int,input().split()))

start = 0
end = max(lst)

while(start<=end):
    mid = (start+end)//2
    lines = 0
    lines = sum(i-mid if i>=mid else 0 for i in lst)
    
    if lines >= n:
        start = mid+1
    else:
        end = mid-1

print(end)