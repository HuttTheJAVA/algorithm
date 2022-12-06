import sys

input = sys.stdin.readline

t = int(input())

didx = [1,0,-1]

## 이미 있는 지뢰 전처리 해야됨.@@

for i in range(t):


    n = int(input())
    bomb_lst = list(map(int,list(input().strip())))
    bomb_state = list(input().strip())

    for idx in range(n):
        if bomb_state[idx] == '*':
            for j in range(3):
                new_idx = idx + didx[j]
                if 0<=new_idx<n:
                    bomb_lst[new_idx] -= 1

    for idx in range(n-1,-1,-1):
        if bomb_lst[idx] and bomb_state[idx] == '#':
            for j in range(3):
                new_idx = idx + didx[j]
                if 0<=new_idx<n and bomb_lst[idx] and bomb_state[new_idx] == '#':
                    can = True
                    for k in range(3):
                        new_new_idx = new_idx + didx[k]
                        if 0<=new_new_idx<n:
                            if not bomb_lst[new_new_idx]:
                                can = False

                    if can:
                        bomb_state[new_idx] = '*'
                        for k in range(3):
                            if 0<=new_idx + didx[k]<n:
                                bomb_lst[new_idx + didx[k]] -= 1

    print(bomb_state.count('*'))                            