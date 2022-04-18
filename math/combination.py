import sys

sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n,m = map(int,input().split())

def fact(n):
    if n == 0:
        return 1
    sum = 1
    for i in range(1,n+1):
        sum *= i
    return sum

print((fact(n)//fact(n-m))//fact(m))