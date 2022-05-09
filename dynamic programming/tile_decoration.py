import sys
input = sys.stdin.readline

n = int(input())

d = [0]*(82)

d[1] = 1
d[2] = 1

def fibo(n):
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n-1)+fibo(n-2)
    return d[n]

fibo(n+1)

print(d[n+1]*2+d[n]*2)