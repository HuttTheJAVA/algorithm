from collections import deque
import sys

input = sys.stdin.readline

n,k = map(int,input().split())

num_lst = list(map(int,list(input().strip())))

R_biggerNum_idx_lst = [None]*(n)
R_biggerNum_idx_lst[-1] = -1
for i in range(n-2,-1,-1):
    if num_lst[i]>num_lst[i+1]:
        qu = deque()
        qu.append(R_biggerNum_idx_lst[i+1])
        while(qu):
            now_idx = qu.popleft()
            if now_idx < 0:
                R_biggerNum_idx_lst[i] = now_idx
                break
            if num_lst[i]>=num_lst[now_idx]:
                qu.append(R_biggerNum_idx_lst[now_idx])
            else:
                R_biggerNum_idx_lst[i] = now_idx
    elif num_lst[i] == num_lst[i+1]:
        R_biggerNum_idx_lst[i] = R_biggerNum_idx_lst[i+1]
    else:
        R_biggerNum_idx_lst[i] = i+1

new_num = ''

for i in range(n):
    if k:
        if k<=(n-1)-i:       # 아직 지울 수 가 지울 기회보다 많으면.
            if R_biggerNum_idx_lst[i] == -1:    # 만약 현재 수가 제일 큰 수면.
                new_num += str(num_lst[i])      # 아직 지울 수가 지울 기회보다 많으니 지우지 않고 다음 번호로 패스 # 현재 제일 큰 수 여도 지울 수가 지울 기회와 같다면 지워야됨. (어째거나 지우는 횟수는 채워야 되므로.)

            elif k>=R_biggerNum_idx_lst[i]-i:
                k-=1
                continue
            else:
                new_num += str(num_lst[i])
        else:
            k -= 1
            continue
    else:
        new_num += str(num_lst[i])

print(new_num)