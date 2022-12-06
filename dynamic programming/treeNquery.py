import sys
sys.setrecursionlimit(10**5+5)
input = sys.stdin.readline

n,r,q = map(int,input().split())

link = [[] for i in range(n+1)]

for i in range(n-1):
    node1,node2 = map(int,input().split())
    link[node1].append(node2)
    link[node2].append(node1)

sub_child_dct = {}
visit = [0]*(n+1)
def count_sub_child(node):
    global sub_child_dct
    if node in sub_child_dct.keys():
        return sub_child_dct[node]
    visit[node] = 1
    my_sub_child_cnt = 1
    for one_hop_child in link[node]:
        if not visit[one_hop_child]:
            my_sub_child_cnt += count_sub_child(one_hop_child)
    sub_child_dct[node] = my_sub_child_cnt
    return sub_child_dct[node]

count_sub_child(r)

for i in range(q):
    query_node = int(input())
    print(sub_child_dct[query_node])

