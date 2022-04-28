import sys

# input = sys.stdin.readline

while(1):
    sentence = input()
    if sentence == '.':
        break
    parenthesis = []
    res = True
    for alp in sentence:
        if alp == '(' or alp == '[':
            parenthesis.append(alp)
        elif alp == ')':
            if parenthesis and parenthesis[-1] == '(':
                parenthesis.pop()
            else:
                res = False
                break
        elif alp == ']':
            if parenthesis and parenthesis[-1] == '[':
                parenthesis.pop()
            else:
                res = False
                break
    if parenthesis:
        res = False
    if res:
        print('yes')
    else:
        print('no')