import sys

input = sys.stdin.readline

n ,m = map(int,input().split())

imigrate_lst = []

for i in range(n):
    imigrate_lst.append(int(input()))

imigrate_lst.sort()

start = 0
end = 1000000000000000000

max_height = sys.maxsize
res = False
while(start<=end):
    mid = (end+start)//2
    person_cnt = 0
    for i in range(len(imigrate_lst)):
        if mid//imigrate_lst[i]:
            person_cnt += mid//imigrate_lst[i]
            if person_cnt >= m:
                if mid<max_height:
                    max_height = mid
                end = mid - 1
                break
        else:
            break
    if person_cnt<m:
        start = mid + 1

print(max_height)