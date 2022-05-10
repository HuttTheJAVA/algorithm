import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())

max_h = 0
min_h = 257

data = []

result = []

for i in range(n):
    lst = list(map(int,input().split()))
    max_h = max(max_h,max(lst))
    min_h = min(min_h,min(lst))
    data.append(lst)

h_dict = {}

for i in range(n):
    for j in range(m):
        if data[i][j] in h_dict:
            h_dict[data[i][j]] += 1
        else:
            h_dict[data[i][j]] = 1

for h in range(min_h,max_h+1):
    time = 0
    remove_cnt = 0
    plus_cnt = 0
    for high in h_dict.keys():
        if high>h:
            remove_cnt += (high-h)*h_dict[high]
            time += ((high-h)*h_dict[high])*2
        elif high<h:
            plus_cnt += (h-high)*h_dict[high]
            time += (h-high)*h_dict[high]

    if plus_cnt>b+remove_cnt:
        continue
    result.append((time,h))

result.sort(key=lambda x:(x[0],-x[1]))
print(result[0][0],result[0][1])