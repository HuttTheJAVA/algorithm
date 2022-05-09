import sys
input = sys.stdin.readline

n,m = map(int,input().split())

s = []

for i in range(n):
    s.append(input())

c = []
cnt = 0

for j in range(m):
    word = input()

    if word in s:
        cnt += 1

print(cnt)