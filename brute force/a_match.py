import sys
input = sys.stdin.readline

n = int(input())

cost = {'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':6}

nums = []

for i in range(99):
    if i<10:
        nums.append('0'+str(i))
    else:
        nums.append(str(i))

def mathcs():
    if n < 22:
        print('impossible')
        return
    for i in nums:
        for j in nums:
            for k in nums:
                if int(i)+int(j)==int(k):
                    hab = 0
                    for num in i:
                        hab += cost[num]
                    for num2 in j:
                        hab += cost[num2]
                    for num3 in k:
                        hab += cost[num3]
                    if hab == n-4:
                        print("{}+{}={}".format(i,j,k))
                        return
    print("impossible")
    return

mathcs()