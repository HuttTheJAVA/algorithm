import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

can = 0

def make_T(s,t):
    global can
    if can:
        return
    if len(s) == len(t):
        if s == t:
            can = 1
        return
    if s+'A' in t or (s+'A')[::-1] in t:
        make_T(s+'A',t)
    if 'B'+s[::-1] in t or ('B'+s[::-1])[::-1] in t:
        make_T('B'+s[::-1],t)

make_T(S,T)

print(can)