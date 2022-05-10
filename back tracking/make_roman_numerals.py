import sys
input = sys.stdin.readline

n = int(input())

rome_num = [1,5,10,50]

rome_set = set()

done_path = []

def rome(n,depth,word):
    if n == depth:
        rome_set.add(word)
        return
    for i in range(4):
        if (depth+1,word+rome_num[i]) in done_path:
            continue
        else:
            done_path.append((depth+1,word+rome_num[i]))
            rome(n,depth+1,word+rome_num[i])


for i in range(4):
    done_path.append((1,rome_num[i]))
    rome(n,1,rome_num[i])

print(len(rome_set))