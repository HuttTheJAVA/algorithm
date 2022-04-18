num = int(input())-1

for i in range(0,1000000):
    
    if num <= 6*i:
        break
    num -= 6*i

print(i+1)