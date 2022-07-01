from collections import deque
from re import S
import sys
input = sys.stdin.readline

n = int(input())

def matchOrderable(order,n,t,l):
    if order == "O(N)":
        time = n
    elif order == "O(N^2)":
        time = n**2
    elif order == "O(N^3)":
        time = n**3
    elif order == "O(2^N)":
        time = 2**n
    elif order == "O(N!)":
        time = 1
        for i in range(1,n+1):
            time *= i
            if time > 10**8*10:
                return "TLE!"
    
    time = int(time*t)
    if time<=l*10**8:
        return "May Pass."
    else:
        return "TLE!"

    
for i in range(n):
    orderable,N,T,L = input().split()
    print(matchOrderable(orderable,int(N),int(T),int(L)))