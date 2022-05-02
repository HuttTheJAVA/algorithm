t = int(input())
info_lst = []

for i in range(t):
    weight,height = map(int,input().split())
    info_lst.append([weight,height])
    
for i in info_lst:
    ranking = 1
    for j in info_lst:
        if i[0] < j[0] and i[1] < j[1]:
            ranking += 1
    print(ranking,end=" ")