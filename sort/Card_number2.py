import sys
input = sys.stdin.readline

n = int(input())

n_lst = list(map(int,input().split()))

m = int(input())

m_lst = list(map(int,input().split()))

result = {}

for i in n_lst:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

for j in m_lst:
    if j in result:
        print(result[j],end=" ")
    else:
        print(0,end=" ")