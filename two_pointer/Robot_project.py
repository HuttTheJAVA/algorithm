import sys
input = sys.stdin.readline

while(1):
    try:
        n = int(input())
        n = n*10000000

        peice_cnt = int(input())

        peices = []

        for i in range(peice_cnt):
            peices.append(int(input()))

        peices.sort()

        head = 0
        tail = len(peices)-1
        res = 1

        while(head<tail):
            two_peice = peices[head]+peices[tail]
            if two_peice == n:
                print(f"yes {peices[head]} {peices[tail]}")
                res = 0
                break
            elif  two_peice > n:
                tail -= 1
            else:
                head += 1

        if res:
            print("danger")
    except:
        break