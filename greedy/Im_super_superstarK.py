import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

survivers = []

for i in range(m):
    lst = list(map(float,input().split()))
    for i in range(0,len(lst),2):
        survivers.append((int(lst[i]),lst[i+1]))

survivers.sort(reverse=True,key = lambda x:x[1])

hab = 0

did  = []
pop = 0
for i in range(len(survivers)):
    if survivers[i][0] not in did:
        hab += survivers[i][1]
        did.append(survivers[i][0])
        pop += 1
    if pop == k:
        break

print(round(hab,1))