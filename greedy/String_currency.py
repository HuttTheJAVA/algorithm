import sys
input = sys.stdin.readline

leng,num = map(int,input().split())

word=  ''

alp = 65

len_word = 0

all_a = leng/num

while(1):
    if all_a<=1 and (leng - len_word)*26>=num:
        if (num-1) - (leng-len_word-1)*26<=0:
            alp = 65
        else:
            alp = 64 + (num - (leng-len_word-1)*26)
        word += chr(alp)
        len_word += 1
        if len_word == leng:
            break
        num -= (alp-64)
    else:
        break

if len_word==leng:
    print(word)
else:
    print('!')