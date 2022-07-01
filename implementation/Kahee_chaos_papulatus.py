from collections import deque
import sys
input = sys.stdin.readline
now_hour,now_minute = map(int,input().split(":"))

six_area = list(map(int,input().split()))

events = int(input())

event_lst = []

is_lock = [0]*6
len_lock = set()
def lock_area():
    if 0<=now_hour<2:
        is_lock[0] = 1
        len_lock.add(1)
    elif 2<=now_hour<4:
        is_lock[1] = 1
        len_lock.add(2)
    elif 4<=now_hour<6:
        is_lock[2] = 1
        len_lock.add(3)
    elif 6<=now_hour<8:
        is_lock[3] = 1
        len_lock.add(4)
    elif 8<=now_hour<10:
        is_lock[4] = 1
        len_lock.add(5)
    elif 10<=now_hour<12:
        is_lock[5] = 1
        len_lock.add(6)

def make_time(command):
    global now_hour
    global now_minute
    if "HOUR" in command:
        now_hour += int(command[0])
    elif "MIN" in command:
        now_minute += int(command[:2])
    now_hour += now_minute//60
    now_minute = now_minute%60
    if now_hour == 12:
        now_hour = 0
    elif now_hour > 12:
        now_hour = now_hour%12

for i in range(events):
    dt,command = input().split()
    dt = float(dt)
    event_lst.append((dt,command))
    if dt<60:
        if command == '^':
            lock_area()
        else:
            make_time(command)
    else:
        break
    if len(len_lock) == 6:
        break


hp = 0

for i in range(len(six_area)):
    if not is_lock[i]:
        hp += six_area[i]

if hp>100:
    print(100)
else:
    print(hp)