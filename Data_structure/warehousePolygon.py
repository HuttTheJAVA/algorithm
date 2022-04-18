import sys
input = sys.stdin.readline

bar_lst = []

n = int(input())

for i in range(n):
    x,h = map(int,input().split())
    bar_lst.append((x,h))

bar_lst.sort()

m2 = 0

p_i = bar_lst.index(max(bar_lst,key= lambda x:x[1]))
p_i_l = p_i
p_i_r = p_i
m2 += bar_lst[p_i][1]

pivot_x = bar_lst[p_i][0]
pivot_x_l = pivot_x

pivot_x_r = pivot_x
collision_l = False
collision_r = False

left_lst = bar_lst[:p_i_l]
right_lst = bar_lst[p_i_r+1:]
while(1):
    if p_i == 0:
        collision_l = True
    if p_i == n-1:
        collision_r = True

    
    
    if left_lst == []:
        collision_l = True
    if collision_l == False:
        next_bar_idx_l = left_lst.index(max(left_lst,key= lambda x:x[1]))
        m2 += (pivot_x_l - left_lst[next_bar_idx_l][0])*left_lst[next_bar_idx_l][1]
        p_i_l = next_bar_idx_l
        pivot_x_l = left_lst[next_bar_idx_l][0]
        left_lst = left_lst[:p_i_l]
       

    
    
    if right_lst == []:
        collision_r = True
    if collision_r == False:
        next_bar_idx_r = right_lst.index(max(right_lst,key= lambda x:x[1]))
        m2 += (right_lst[next_bar_idx_r][0]-pivot_x_r)*right_lst[next_bar_idx_r][1]
        p_i_r = next_bar_idx_r
        pivot_x_r = right_lst[p_i_r][0]
        right_lst = right_lst[p_i_r+1:]

            
    if collision_r == True and collision_l == True:
        break

print(m2)