import sys
input = sys.stdin.readline

while(1):
    Estation = int(input())
    if not Estation:
        break
    station_lst = []
    for i in range(Estation):
        dist = int(input())
        station_lst.append(dist)
    station_lst.sort()

    reach = True

    for i in range(1,len(station_lst)):
        if station_lst[i]-station_lst[i-1]>200:
            reach = False
            break
    if (1422-station_lst[-1])*2>200:
        reach = False

    if reach:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")