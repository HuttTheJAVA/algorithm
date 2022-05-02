import sys
input = sys.stdin.readline

n = int(input())


def do_cal(cnt,word,leng,idx):
    global n_lst
    if cnt == leng-1:
        if eval(word.replace(" ","")) == 0:
            word_lst.append(word)
        return
    
    for i in range(idx+1,leng):
        do_cal(cnt+1,word+'+'+str(n_lst[i]),leng,i)
        do_cal(cnt+1,word+'-'+str(n_lst[i]),leng,i)
        do_cal(cnt+1,word+' '+str(n_lst[i]),leng,i)

for i in range(n):

    word_lst = []
    
    leng = int(input())

    n_lst = [i for i in range(1,leng+1)]

    for i in range(len(n_lst)):
        do_cal(0,str(n_lst[i]),leng,i)
    
    word_lst.sort()

    for line in word_lst:
        print(line)
    print()