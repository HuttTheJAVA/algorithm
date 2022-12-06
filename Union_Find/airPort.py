import sys
from collections import deque
input = sys.stdin.readline

G = int(input())
P = int(input())

end_gate_lst = []

gate = [i for i in range(G+1)]

for i in range(P):
    end_gate_lst.append(int(input()))

def find(x):
    if gate[x] == x:
        return gate[x]
    
    gate[x] = find(gate[x])

    return gate[x]

def union(x,y):
    if gate[x] == gate[y]:
        return
    parent_gate_x = find(x)
    parent_gate_y = find(y)

    if parent_gate_x<=parent_gate_y:
        gate[parent_gate_y] = parent_gate_x
    else:
        gate[parent_gate_x] = parent_gate_y
    
    min_val = min(parent_gate_x,parent_gate_y)
    return min_val # 이 리턴값이 0이면 더 이상 진행불가

cnt_dock = 0

for end in end_gate_lst:
    y = find(gate[end])
    if y-1<0:
        break
    x = find(gate[y-1])
    res = union(x,y)
    cnt_dock += 1

print(cnt_dock)