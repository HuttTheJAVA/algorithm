n,m = list(map(int,input().split()))

s=[]

def dfs(s):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return

    for i in range(1,n+1):
        if i in s:
            continue
        if s:
            if i<s[-1]:
                continue
        s.append(i)
        dfs(s)
        s.pop()

dfs(s)