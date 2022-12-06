import sys

input = sys.stdin.readline

n,k = map(int,input().split())

bak = [0]*k

if n>=(k*(k+1))//2: # 2로 나눠도 무조건 정수값((홀수 * 짝수 = 짝수) / 2 = 짝수)임. // 하는 이유는 정수간 연산하기 위함.
    bak = [i for i in range(1,k+1)]
    n -= (k*(k+1))//2
    if n//k:
        n -= (n//k)*k
        for i in range(len(bak)):
            bak[i] += n//k
    if n:
        for i in range(len(bak)-1,-1,-1):
            if n:
                bak[i] += 1
                n -= 1
            else:
                break
    print(bak[-1] - bak[0])
else:
    print(-1)
