import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

deck = deque()

for i in range(1,n+1):
    deck.append(i)

while(len(deck) != 1):
    throw = deck.popleft()
    shuffle  = deck.popleft()
    deck.append(shuffle)

print(deck[0])