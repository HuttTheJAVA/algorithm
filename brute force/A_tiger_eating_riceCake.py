import sys
input = sys.stdin.readline

def fibo(a,b,n,k):
    for i in range(n-2):
        a,b = b,a+b
        
    if b == k:
        return True

def h():
    d,k = map(int,input().split())
    for i in range(1,k):
        for j in range(i+1,k+1):
            if fibo(i,j,d,k):
                print(i)
                print(j)
                return

h()  