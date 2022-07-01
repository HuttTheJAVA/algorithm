from collections import deque
import sys
input = sys.stdin.readline

find = input().strip()
find = find.replace(" ","")

init_clock_num = 10000

for i in range(4):
    init_clock_num = min(init_clock_num,int(find[i:len(find)+1]+find[0:i]))

Clock_number_lst = set()

def makeClockNum(lst):
    clockNum = 10000
    for i in range(4):
        clockNum = min(clockNum,int(lst[i:len(lst)+1]+lst[0:i]))
    return clockNum

for i in range(1111,10000):
    if '0' not in str(i):
        Clock_number_lst.add(int(makeClockNum(str(i))))

Clock_number_lst = list(Clock_number_lst)

Clock_number_lst.sort()

print(Clock_number_lst.index(init_clock_num)+1)