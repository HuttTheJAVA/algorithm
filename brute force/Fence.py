import sys
from collections import deque
import heapq
input = sys.stdin.readline

n = int(input())

trees = []

for i in range(n):
    x,y,resource = map(int,input().split())
    trees.append((x,y,resource))

min_cut = 41
for i in range(n-1):
    x1,y1,resource1 = trees[i]
    for j in range(i+1,n):
        x2,y2,resource2 = trees[j]
        x_lst = [x1,x2]
        y_lst = [y1,y2]
        x_lst.sort()
        y_lst.sort()
        this_case_cut = 0
        r_u_in = []         # 힙큐로 구현하자 매번 정렬하지말고
        r_u_not = []        # 얘는 어차피 다 써야되니까 힙큐 x
        start_x,end_x = x_lst[0],x_lst[1]
        start_y,end_y = y_lst[0],y_lst[1]
        if not (end_x - start_x) or not (end_y - start_y):
            rectangle = 1*(end_x - start_x) + 1*(end_y - start_y)
        else:
            rectangle = 2*(end_x - start_x) + 2*(end_y - start_y)
        
        for z in range(n):
            if z != i and z != j:
                x3,y3,resource3 = trees[z]
                if start_x<=x3<=end_x and start_y<=y3<=end_y:
                    heapq.heappush(r_u_in,-resource3)
                else:
                    r_u_not.append(resource3)
        for out_tree in r_u_not:
            rectangle -= out_tree
        this_case_cut = len(r_u_not)
        if rectangle>0:
            if r_u_in:
                while(r_u_in and rectangle>0):
                    val = -heapq.heappop(r_u_in)
                    rectangle -= val
                    this_case_cut += 1
        if rectangle<=0:
            min_cut = min(min_cut,this_case_cut)
if n > 2:
    for i in range(n-2):
        x1,y1,resource1 = trees[i]
        for j in range(i+1,n-1):
            x2,y2,resource2 = trees[j]
            for k in range(j+1,n):
                x3,y3,resource3 = trees[k]
                x_lst = [x1,x2,x3]
                y_lst = [y1,y2,y3]
                x_lst.sort()
                y_lst.sort()
                this_case_cut = 0
                r_u_in = []
                r_u_not = []
                start_x,end_x = x_lst[0],x_lst[-1]
                start_y,end_y = y_lst[0],y_lst[-1]
                if not (end_x-start_x) or not (end_y-start_y):
                    rectangle = 1*(end_x-start_x) + 1*(end_y-start_y)
                else:
                    rectangle = 2*(end_x-start_x) + 2*(end_y-start_y)
                
                for l in range(n):
                    if l != i and l != j and l != k:
                        x4,y4,resource4 = trees[l]
                        if start_x<=x4<=end_x and start_y<=y4<=end_y:
                            heapq.heappush(r_u_in,-resource4)
                        else:
                            r_u_not.append(resource4)
                for out_tree in r_u_not:
                    rectangle -= out_tree
                this_case_cut = len(r_u_not)
                if rectangle>0:
                    if r_u_in:
                        while(r_u_in and rectangle>0):
                            val = -heapq.heappop(r_u_in)
                            rectangle -= val
                            this_case_cut += 1
                if rectangle <= 0:
                    min_cut = min(min_cut,this_case_cut)
    if n >= 4:
        for i in range(n-3):
            x1,y1,resource1 = trees[i]
            for j in range(i+1,n-2):
                x2,y2,resource2 = trees[j]
                for k in range(j+1,n-1):
                    x3,y3,resource3 = trees[k]
                    for l in range(k+1,n):
                        x4,y4,resource4 = trees[l]
                        x_lst = [x1,x2,x3,x4]
                        y_lst = [y1,y2,y3,y4]
                        x_lst.sort()
                        y_lst.sort()
                        this_case_cut = 0
                        r_u_in = []
                        r_u_not = []
                        start_x,end_x = x_lst[0],x_lst[-1]
                        start_y,end_y = y_lst[0],y_lst[-1]
                        if not (end_x-start_x) or not(end_y-start_y):
                            rectangle = 1*(end_x-start_x) + 1*(end_y-start_y)
                        else:
                            rectangle = 2*(end_x-start_x) + 2*(end_y-start_y)
                        

                        for m in range(n):
                            if m != i and m != j and m != k and m != l:
                                x5,y5,resource5 = trees[m]
                                if start_x<=x5<=end_x and start_y<=y5<=end_y:
                                    heapq.heappush(r_u_in,-resource5)
                                else:
                                    r_u_not.append(resource5)
                        for out_tree in r_u_not:
                            rectangle -= out_tree
                        this_case_cut = len(r_u_not)
                        if rectangle>0:
                            if r_u_in:
                                while(r_u_in and rectangle>0):
                                    val = -heapq.heappop(r_u_in)
                                    rectangle -= val
                                    this_case_cut += 1
                        if rectangle <= 0:
                            min_cut = min(min_cut,this_case_cut)
if min_cut == 41:
    min_cut = n-1
print(min_cut)