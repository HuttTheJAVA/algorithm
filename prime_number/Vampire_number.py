import sys
input = sys.stdin.readline

while(1):
    number = int(input())
    if not number:
        break
    is_vampire_num = False
    for i in range(number,1000256):
        for j in range(2,int(i**0.5)+1):
            if not i%j:
                compare_string = str(j)+str(i//j)
                lst1 = list(str(i))
                lst2 = list(compare_string)
                lst1.sort()
                lst2.sort()
                if lst1 == lst2:
                    is_vampire_num = True
                    print(i)
                    break
        if is_vampire_num:
            break