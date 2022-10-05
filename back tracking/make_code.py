import sys

input = sys.stdin.readline

l,c = map(int,input().split())

alp_lst = list(input().split())

alp_lst.sort()

zaums = ['a','e','i','o','u']

def dfs(word,idx):
    if len(word) == l:
        cnt = 0
        for zaum in zaums:
            if zaum in word:
                cnt += 1
        other_cnt = l-cnt
        if 1<=cnt and other_cnt>=2:
            print(word)
        return
    
    for i in range(idx+1,len(alp_lst)):
        dfs(word+alp_lst[i],i)


for i in range(len(alp_lst)):
    dfs(alp_lst[i],i)