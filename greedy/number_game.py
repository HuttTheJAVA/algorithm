import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
  n = int(input())
  cnt = 0
  res = True
  while(n>9):
    res = False
    for i in range(9,1,-1):
      if not n%i:
        n //= i
        cnt += 1
        res = True
        break
    if not res:
      break

  if n<10:
    print(cnt+1)
  else:
    print(-1)