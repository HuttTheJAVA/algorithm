from collections import deque
import sys
input = sys.stdin.readline


T = int(input())


for t in range(T):
    buffer = []

    temp_buffer = deque()
    inputs = input().strip()
    for i in range(len(inputs)):
        if inputs[i] == "<":
            if buffer:
                temp_buffer.appendleft(buffer.pop())
        elif inputs[i] == ">":
            if temp_buffer:
                buffer.append(temp_buffer.popleft())
        elif inputs[i] == "-":
            if buffer:
                buffer.pop()
        else:
            buffer.append(inputs[i])
    temp_buffer = list(temp_buffer)
    
    print(''.join(buffer)+''.join(temp_buffer))