import sys
input = sys.stdin.readline
import math as m


X,Y = map(int,input().split())

if X>=Y:
    print(X+Y+m.floor(Y//10))
else:
    print(X+Y+m.floor(X//10))