from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
men = list(map(int,input().split()))
women = list(map(int,input().split()))

mens_smaller_women = []
mens_taller_women = []
womens_smaller_men = []
womens_taller_men = []

for i in range(len(men)):
    if men[i] < 0:
        mens_smaller_women.append(abs(men[i]))
    else:
        mens_taller_women.append(men[i])
    if women[i] < 0:
        womens_smaller_men.append(abs(women[i]))
    else:
        womens_taller_men.append(women[i])

mens_taller_women.sort()
mens_taller_women = deque(mens_taller_women)
mens_smaller_women.sort()
mens_smaller_women = deque(mens_smaller_women)
womens_smaller_men.sort()
womens_smaller_men = deque(womens_smaller_men)
womens_taller_men.sort()
womens_taller_men = deque(womens_taller_men)

cnt = 0

while(mens_taller_women and womens_smaller_men):
    if mens_taller_women[0] >= womens_smaller_men[0]:
        womens_smaller_men.popleft()
    else:
        womens_smaller_men.popleft()
        mens_taller_women.popleft()
        cnt += 1

while(mens_smaller_women and womens_taller_men):
    if mens_smaller_women[0] <= womens_taller_men[0]:
        mens_smaller_women.popleft()
    else:
        womens_taller_men.popleft()
        mens_smaller_women.popleft()
        cnt += 1

print(cnt)