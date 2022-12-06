import sys

input = sys.stdin.readline

word = input().strip()

bit_mask = [0]*len(word)

def recursion_compress():
    global word
    global bit_mask
    stack = []
    length = 0
    heads = []
    lengs = []
    for i in range(len(word)):
        if not bit_mask[i]:
            bit_mask[i] = 1
            if word[i] == '(':
                if stack:           # stack에 숫자가 없다면 K(Q)의 형식에 어긋난다 K는 분명히 한자리 정수라고 했다. 0이든 어떤값이 됐건간에..
                    head = stack.pop()
                    length -= 1
                # else:
                #     head = 1        # (245)(2244) 이 경우는 없는 경운가? 문제에서 보면 K(Q)의 형태로 압축할 수 있다고 말한 것을 보면 여는 괄호 앞에는 무조건 수가 오는 것 같다..
                    leng = recursion_compress()
                    heads.append(head)
                    lengs.append(leng)
            elif word[i] == ')':
                if heads:
                    val = len(stack)
                    while(heads):
                        val += heads.pop()*lengs.pop()
                    return val
                else:
                    return len(stack)
            else:
                stack.append(int(word[i]))
                length += 1
    if heads:
        val = len(stack)
        while(heads):
            val += heads.pop()*lengs.pop()
        return val
    else:
        return len(stack)

print(recursion_compress())