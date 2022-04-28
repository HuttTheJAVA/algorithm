import sys
input = sys.stdin.readline

n = int(input())

r = int(input())

group = [[] for i in range(n)]

for i in range(r):
    a,b = map(int,input().split())
    group[a-1].append(b)
    group[b-1].append(a)

invite = set()

for friends in group[0]:
    invite.add(friends)
    for friends2 in group[friends-1]:
        invite.add(friends2)
if 1 in invite:
    print(len(invite)-1)
else:
    print(len(invite))