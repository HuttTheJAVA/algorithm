import sys
import heapq
input =sys.stdin.readline

n = int(input())

word_lst = []

for i in range(n):
    word_lst.append(input().strip())

alp_dct = {}        # 알파벳별 각 자리수 카운트 딕셔너리

for word in word_lst:
    word = word[::-1]
    for i in range(len(word)):
        try:
            a = alp_dct[word[i]]
        except:
            alp_dct[word[i]] = [0]*8
        
        alp_dct[word[i]][i] += 1

assign_num_2_alp = {}   # 알파벳별 할당받는 숫자 저장 딕셔너리

for num in range(9,-1,-1):
    queue_4_waiting_assign = []         # 숫자 할당 받기위한 알파벳 큐 (각 자리별 총합,알파벳) 으로 저장됨  @@ 힙큐로 push,pop하자
    for alp in alp_dct:
        try:
            b = assign_num_2_alp[alp]
        except:     # 할당받은 딕셔너리에 조회되지 않는다면
            hab = 0
            for i in range(len(alp_dct[alp])):
                hab += 10**i * num * alp_dct[alp][i]
            heapq.heappush(queue_4_waiting_assign,(-hab,alp))
    if queue_4_waiting_assign:
        val,alp = heapq.heappop(queue_4_waiting_assign)
        assign_num_2_alp[alp] = num
    else:
        break

total_sum = 0

for word in word_lst:
    str_num = ''
    for i in range(len(word)):
        str_num += str(assign_num_2_alp[word[i]])
    total_sum += int(str_num)

print(total_sum)