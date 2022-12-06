from collections import deque
import sys
import copy
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    phone_lst = []
    phone_dct = {}
    cant = False
    for i in range(n):
        number = input().strip()
        phone_lst.append(number)
    phone_lst.sort(key=lambda x:len(x))
    for i in range(len(phone_lst)):
        for j in range(len(phone_lst[i])):
            try:
                a = phone_dct[phone_lst[i][:j]]
                cant = True
            except:
                pass
            if cant:
                break
        if cant:
            break
        else:
            phone_dct[phone_lst[i]] = 1
    if cant:
        print("NO")
    else:
        print("YES")
