import sys
input = sys.stdin.readline

n = int(input())

num_price = list(map(int,input().split()))

money = int(input())

most_cheap_number = None
most_cheap_cost = 970623

for i in range(len(num_price)):
    if num_price[i]<=most_cheap_cost:
        most_cheap_number = i
        most_cheap_cost = num_price[i]

number = ''

while(1):
    next_num = None    
    global_remain_leng = -1
    for i in range(len(num_price)):
        if not len(number) and i == 0:
            continue
        if num_price[i]<=money:
            local_remain_leng = (money-num_price[i])//most_cheap_cost
            if local_remain_leng>=global_remain_leng:
                next_num = i
                global_remain_leng = local_remain_leng
    if global_remain_leng > -1:
        number += str(next_num)
        money -= num_price[next_num]
    else:
        break

if not len(number):
    number += str(most_cheap_number)

print(number)
