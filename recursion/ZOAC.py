import sys
input = sys.stdin.readline

word = list(input().strip())

is_print = [0]*len(word)

def search_first_alp(is_print,start,end):
    global word
    pivot_idx = None
    pivot_val = 100000000
    for i in range(start,end):
        if ord(word[i])<pivot_val and not is_print[i]:
            pivot_val = ord(word[i])
            pivot_idx = i
    if pivot_idx == None:
        return
    is_print[pivot_idx] = 1
    for i in range(len(word)):
        if is_print[i]:
            print(word[i],end="")
    print()
    search_first_alp(is_print,pivot_idx+1,len(word))
    search_first_alp(is_print,start,pivot_idx)

search_first_alp(is_print,0,len(is_print))