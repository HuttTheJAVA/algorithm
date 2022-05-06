import sys
input = sys.stdin.readline

n = int(input())

order = ['add','remove','check','toggle','all','empty']

dp = [0]*20

s = []

def add(x):
    if not dp[x-1]:
        dp[x-1] = 1

def remove(x):
    if dp[x-1]:
        dp[x-1] = 0

def check(x):
    if dp[x-1]:
        return 1
    else:
        return 0

def toggle(x):
    if dp[x-1]:
        dp[x-1] = 0
    else:
        dp[x-1] = 1

def all():
    for i in range(len(dp)):
        dp[i] = 1

def empty():
    for i in range(len(dp)):
        dp[i] = 0

for i in range(n):
    a = input().strip()
    if " " in a:
        a,b = a.split()
        b = int(b)
    if a == order[0]:
        add(b)
    elif a == order[1]:
        remove(b)
    elif a == order[2]:
        print(check(b))
    elif a == order[3]:
        toggle(b)
    elif a == order[4]:
        all()
    elif a == order[5]:
        empty()