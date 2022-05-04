import sys
input = sys.stdin.readline

my_card = int(input())
my_lst = list(map(int,input().split()))

find_card = int(input())
find_lst = list(map(int,input().split()))

my_lst.sort()

def bi_search(lst,val,start,end):
    
    if start>end:
        return 0
    mid = (start+end)//2
    if val == lst[mid]:
        return 1
    elif val<lst[mid]:
        end = mid-1
        return bi_search(lst,val,start,end)
    else:
        start = mid+1
        return bi_search(lst,val,start,end)

for cards in find_lst:
    print(bi_search(my_lst,cards,0,len(my_lst)-1),end=" ")