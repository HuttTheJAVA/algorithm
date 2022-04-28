n_lst = list(range(2,246913))

def sosu(num):
    if num<=1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False

    return True

memo = []

for i in n_lst:
    if sosu(i):
        memo.append(i)

while(1):
    n = int(input())
    count = 0
    if n == 0:
        break

    for val in memo:
        if n<val<=(2*n):
            count += 1
    print(count)