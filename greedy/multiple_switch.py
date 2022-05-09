import sys
import math as m
input = sys.stdin.readline

word = list(input().strip())

def switch(idx):
    if word[idx] == 'Y':
        word[idx] = 'N'
    else:
        word[idx] = 'Y'

cnt = 0

for i in range(len(word)):
    if word[i] == 'Y':
        switch(i)
        pivot = i+(i+1)
        while(pivot<len(word)):
            switch(pivot)
            pivot += (i+1)
        cnt += 1

if ''.join(word) == 'N'*len(word):
    print(cnt)
else:
    print(-1)