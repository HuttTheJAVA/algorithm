import sys
input = sys.stdin.readline

INF = (1e9)

n,made = map(int,input().split())

def bfs(n,m):
    cnt = 1
    while(n<m):
        if str(m)[-1] == '1':
            m = int(str(m)[:-1])
            cnt += 1
        else:
            if m%2 == 0:
                m = m//2
                cnt += 1
            else:
                return -1
    
    if n == m:
        return cnt
    return -1
print(bfs(n,made))