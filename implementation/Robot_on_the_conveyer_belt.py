import sys
input = sys.stdin.readline

n,k = map(int,input().split())

durab_lst = list(map(int,input().split()))

robot_location = [0]*n

on_rail_cnt = 0

retire = 0

stage = 0

def rotate_rail():
    global stage
    global on_rail_cnt
    global durab_lst
    global robot_location
    stage += 1
    durab_lst = [durab_lst[-1]] + durab_lst[:-1]
    robot_location = [0] + robot_location[:-1]
    if robot_location[-1]:
        robot_location[-1] = 0
        on_rail_cnt -= 1

while(retire<k):
    rotate_rail()
    if on_rail_cnt:
        for i in range(len(robot_location)-2,-1,-1):
            if robot_location[i] and durab_lst[i+1] and not robot_location[i+1]:
                robot_location[i] = 0
                durab_lst[i+1] -= 1
                if not durab_lst[i+1]:
                    retire += 1
                if i+1 == n-1:
                    on_rail_cnt -= 1 
                    continue
                robot_location[i+1] = 1
    if durab_lst[0]:
        robot_location[0] = 1
        durab_lst[0] -= 1
        on_rail_cnt += 1
        if not durab_lst[0]:
            retire += 1

print(stage)