import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())

arrow = list(input().split())

min_val = [INF]

max_val = [-1]

def bruteForce(x,arr,depth,word):
    global min_val
    global max_val
    if len(word) == len(arr)+1:
        if int(word)<int(min_val[0]):
            min_val = [word]
        if int(word)>int(max_val[0]):
            max_val = [word]
        return

    for i in range(10):
        if arr[depth] == '>':
            if x>i and str(i) not in word:
                bruteForce(i,arr,depth+1,word+str(i))
        elif arr[depth] == '<':
            if x<i and str(i) not in word:
                bruteForce(i,arr,depth+1,word+str(i))

for i in range(10):
    bruteForce(i,arrow,0,str(i))

print(max_val[0])
print(min_val[0])