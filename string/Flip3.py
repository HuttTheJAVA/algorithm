import sys
input = sys.stdin.readline

word = input().strip()

head = word[0]

for i in range(1,len(word)):
    if ord(head)>=ord(word[i]):
        head = word[i]
        new_word = word[i] + word[:i] + word[i+1:]
        word = new_word

print(word)