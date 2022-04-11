import sys
input = sys.stdin.readline

N,M = map(int,input().split())

DNA_lst = []

for i in range(N):
    DNA = input()
    DNA_lst.append(DNA)

differ = 0

strng = ""

for i in range(M):
    dct = {}
    for DNAS in DNA_lst:
        if DNAS[i] in dct:
            dct[DNAS[i]] += 1
        else:
            dct[DNAS[i]] = 1
    dct = list(dct.items())
    dct.sort(key=lambda x:(-x[1],x[0]))
    strng = strng+dct[0][0]
    differ += N-dct[0][1]

print(strng)
print(differ)