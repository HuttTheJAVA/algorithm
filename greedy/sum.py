from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

words = []

for i in range(n):
    words.append(input().strip())

alp_dct = {}

on_front = {}

for word in words:
    leng = len(word)
    for i in range(len(word)):
        try:
            alp_dct[word[i]][leng-i] += 1
        except:
            alp_dct[word[i]] = [0]*13
            alp_dct[word[i]][leng-i] += 1
    
    try:
        a = on_front[word[0]]
    except:
        on_front[word[0]] = 1

num = deque()

for i in range(9,-1,-1):
    num.append(i)

left_keys = []

for ki in alp_dct.keys():
    left_keys.append(ki)

alp_map_num_dct = {}

for _ in range(len(alp_dct)):
    alp_hab = [-1]*10
    for l_ki in left_keys:
        alp_hab[ord(l_ki)-ord('A')] = 0
        for digit_idx in range(len(alp_dct[l_ki])):
            if alp_dct[l_ki][digit_idx]:
                alp_hab[ord(l_ki)-ord('A')] += alp_dct[l_ki][digit_idx]*num[0]*10**(digit_idx-1)
    max_alp_hap = -1
    max_idx = -1
    for alp in range(len(alp_hab)):
        if alp_hab[alp] != -1:
            if alp_hab[alp]>max_alp_hap:
                max_alp_hap = alp_hab[alp]
                max_idx = alp
    
    alp_map_num_dct[chr(ord('A')+max_idx)] = num.popleft()
    left_keys.remove(chr(ord('A')+max_idx))

alp_num_lst = []

for i in alp_map_num_dct.keys():
    alp_num_lst.append((i,alp_map_num_dct[i]))

alp_num_lst.sort(key=lambda x:(x[1]))

if alp_num_lst[0][1] == 0:
    try:
        a = on_front[alp_num_lst[0][0]]
        done = False
        for i in range(len(alp_num_lst)-1):
            try:
                a = on_front[alp_num_lst[i][0]]
                alp_map_num_dct[alp_num_lst[i][0]],alp_map_num_dct[alp_num_lst[i+1][0]] = alp_map_num_dct[alp_num_lst[i+1][0]],alp_map_num_dct[alp_num_lst[i][0]]
            except:
                break

    except:
        pass

hab = 0

for word in words:
    number = ''
    for alp in word:
        number += str(alp_map_num_dct[alp])
    hab += int(number)

print(hab)
