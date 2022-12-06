import sys
input =sys.stdin.readline

g = int(input())

x = 1
has = False
while(1):
    calc = (x**2-g)**0.5
    gap = x**2 - (x-1)**2
    if x**2-g > 0 and int(calc) == calc:
        print(x)
        has = True
    x += 1
    if gap > 100000:
        break
if not has:
    print(-1)