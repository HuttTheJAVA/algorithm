import sys
input= sys.stdin.readline


n = int(input())

one = 1
two = 1
three = 1

result = 0

if n<4:
    print(1)
else:

    for i in range(4,n):
        one,two,three = two,three,one+three

    print(one+three)