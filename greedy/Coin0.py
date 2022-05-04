import sys
input = sys.stdin.readline

n,m = map(int,input().split())

m_lst = []
for i in range(n):
    money = int(input())
    m_lst.append(money)

m_lst.sort(reverse=True)

count = 0

for i in m_lst:
    if m//i >= 1:
        count += (m//i)
        m = m-(m//i)*i
    if m == 0:
        break
print(count)