def hanoi(n,start,via,to):

    if n==1:
        print(start,to)
    
        return
    hanoi(n-1,start,to,via)
    print(start,to)

    hanoi(n-1,via,start,to)



n = int(input())
k = 1
for i in range(1,n):
    k += 2**i
print(k)
hanoi(n,1,2,3)