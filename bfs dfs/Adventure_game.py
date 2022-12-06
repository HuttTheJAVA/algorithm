from collections import deque
import sys
input = sys.stdin.readline

while(1):

    n = int(input())

    if not n:
        break
    
    room_info = [[None]]

    max_money_history = [-1]*(n+1)

    for i in range(n):
        room_info.append(list(input().split()))

    for  i in range(1,n+1):
        for j in range(1,len(room_info[i])):
            room_info[i][j] = int(room_info[i][j])

    gold = 0

    qu = deque()
    
    if room_info[1] != 'T':
        gold = max(gold,room_info[1][1])
        qu.append((1,gold))
        max_money_history[1] = gold
    
    res = "No"

    while(qu):
        room,gold = qu.popleft()
        if room == n:
            res = "Yes"
            break
        for next_room in room_info[room][2:-1]:
            if room_info[next_room][0] == 'T':
                if gold >= room_info[next_room][1] and max_money_history[next_room]<gold-room_info[next_room][1]:
                    max_money_history[next_room] = gold-room_info[next_room][1]
                    qu.append((next_room,gold-room_info[next_room][1]))
            else:
                new_gold = max(gold,room_info[next_room][1])
                if max_money_history[next_room] < new_gold:
                    max_money_history[next_room] = new_gold
                    qu.append((next_room,new_gold))
    print(res)