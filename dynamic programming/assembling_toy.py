import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

edge_dct = {}

child_dct = {}

node_bluePrint_dct = {}

for i in range(1,n+1):
    child_dct[i] = []
    node_bluePrint_dct[i] = 0

for i in range(m):
    x,y,k = map(int,input().split())
    key = str(x)+','+str(y)
    edge_dct[key] = k%2147483647
    child_dct[x].append(y)

def dfs(node):
    global child_dct
    global need_cnt
    global edge_dct
    my_bluePrintLst = [0]*(n+1)

    if node_bluePrint_dct[node] != 0:
        return node_bluePrint_dct[node]

    if not len(child_dct[node]):
        my_bluePrintLst[node] += 1
        node_bluePrint_dct[node] = my_bluePrintLst
        return my_bluePrintLst

    for child in child_dct[node]:
        key = str(node)+','+str(child)
        childBluePrintLst = dfs(child)
        for idx in range(len(childBluePrintLst)):
            my_bluePrintLst[idx] += (edge_dct[key]*childBluePrintLst[idx])%2147483647
    
    node_bluePrint_dct[node] = my_bluePrintLst

    return node_bluePrint_dct[node]

finalBluePrintLst = dfs(n)

for i in range(len(finalBluePrintLst)):
    if finalBluePrintLst[i]:
        print(i,finalBluePrintLst[i])