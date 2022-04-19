import sys

input = sys.stdin.readline

n = int(input())

height_lst = list(map(int,input().split()))

left_heigher_building = [0]*len(height_lst)

for i in range(1,len(height_lst)):
    pivot = i-1
    while(1):
        if height_lst[pivot] > height_lst[i]:
            left_heigher_building[i] = pivot + 1
            break
        elif height_lst[pivot] == height_lst[i]:
            left_heigher_building[i] = left_heigher_building[pivot]
            break
        elif height_lst[pivot] < height_lst[i]:
            if not left_heigher_building[pivot]:
                break
            elif height_lst[i] > height_lst[left_heigher_building[pivot]-1]:
                pivot = left_heigher_building[pivot] - 1
            elif height_lst[i] == height_lst[left_heigher_building[pivot]-1]:
                left_heigher_building[i] = left_heigher_building[left_heigher_building[pivot]-1]
                break
            else:
                left_heigher_building[i] = left_heigher_building[pivot]
                break
            
print(*left_heigher_building)