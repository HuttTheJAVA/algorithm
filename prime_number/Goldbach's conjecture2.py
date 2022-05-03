import sys

input = sys.stdin.readline

total = [0]*(10001)

n = int(input())
n_lst = []

for i in range(n):
    n_lst.append(int(input()))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    
    return n


for i in range(2,10000):
    num = isPrime(i)
    if num != False:
        total[num] = 1
    
for j in n_lst:
    sosu = j//2
    if total[sosu] == 1:
        print(sosu,sosu)
        continue
    while(1):
        sosu -= 1
        second_sosu = j-sosu
        if total[sosu] != 0 and total[second_sosu] != 0:
            print(sosu,second_sosu)
            break