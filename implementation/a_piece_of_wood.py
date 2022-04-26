import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))

while(lst != [1,2,3,4,5]):
    for i in range(len(lst)-1):
        chage = False
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1] = lst[i+1],lst[i]
            chage = True
        if chage:
            for j in lst:
                print(j,end=" ")
            print()