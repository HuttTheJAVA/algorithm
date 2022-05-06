import sys
input = sys.stdin.readline


n = int(input())

for i in range(n):
    leng = int(input())
    n_lst = list(map(int,input().split()))
    word = []
    reword = []
    max_val = [n_lst.pop(n_lst.index(max(n_lst)))]
    n_lst.sort(reverse=True)
    while(1):
        if n_lst:
            word.append(n_lst.pop())
        if n_lst:
            reword.append(n_lst.pop())
        if not n_lst:
            break
    
    result = word+max_val+reword[::-1]
    max_chai = -1
    for i in range(len(result)-1):
        if abs(result[i]-result[i+1])>max_chai:
            max_chai = abs(result[i]-result[i+1])
    print(max_chai)