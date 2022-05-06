import sys
input = sys.stdin.readline

n = int(input())

n_lst = []
group = []
for i in range(n):
    n_lst.append(int(input()))

n_lst.sort()

for i in range(n//3):
    
    for j in range(3):
        group.append(n_lst.pop())
    

don = 0

for j in range(len(group)):
    if (j+1)%3==0:
        continue
    don += group[j]

print(don+sum(n_lst))