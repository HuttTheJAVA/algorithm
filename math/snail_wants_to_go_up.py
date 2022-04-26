import math as m
a,b,v = map(int,input().split())

print(m.ceil(1+(v-a)/(a-b)))