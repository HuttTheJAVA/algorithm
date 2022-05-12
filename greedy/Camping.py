import sys

input = sys.stdin.readline
case = 1
while(1):
  L,P,V = map(int,input().split())
  if not(L or P or V):
    break
  quotient = V//P
  ans = L*quotient
  V -= P*quotient
  if V>L:
    ans += L
  else:
    ans += V
  print(f"Case {case}: {ans}")
  case += 1