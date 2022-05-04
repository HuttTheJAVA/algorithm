import sys

input = sys.stdin.readline

n,k = map(int,input().split())

fact_lst = [1]*1001

for i in range(2,len(fact_lst)):
    fact_lst[i] = i*fact_lst[i-1]

print((fact_lst[n]//(fact_lst[k]*fact_lst[n-k]))%10007)