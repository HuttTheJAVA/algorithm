import sys
input = sys.stdin.readline

n = int(input())

init_nums = [2,3,5,7]
after_nums = [1,3,5,7,9]

def make_amazing_prime_number(num,leng):
    if len(str(num)) == leng:
        print(num)
        return

    for after in after_nums:
        res = True
        new_num = int(str(num)+str(after))
        for i in range(2,int(new_num**0.5)+1):
            if not new_num%i:
                res = False
                break
        if res:
            make_amazing_prime_number(new_num,leng)


for init in init_nums:
    make_amazing_prime_number(init,n)