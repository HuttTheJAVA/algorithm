import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    word = list(input().strip())
    one_pointer = 0
    two_pointer = len(word)-1
    one_more_chance = 0
    do_one_more_time_for_left_side = 0

    while(one_pointer<=two_pointer):
        if word[one_pointer] == word[two_pointer]:
            one_pointer += 1
            two_pointer -= 1
        else:
            if not one_more_chance:
                if two_pointer - 1 >=0 and word[one_pointer] == word[two_pointer-1]:
                    if one_pointer+1<len(word) and word[one_pointer+1] == word[two_pointer]:
                        do_one_more_time_for_left_side = 1
                    two_pointer -= 1
                    one_more_chance = 1
                elif one_pointer+1<len(word) and word[one_pointer+1] == word[two_pointer]:
                    one_pointer += 1
                    one_more_chance = 1
                else:
                    one_more_chance = 2
                    break
            else:
                one_more_chance = 2
                break
    
    if do_one_more_time_for_left_side:
        temp = one_more_chance
        one_pointer = 0
        two_pointer = len(word)-1
        one_more_chance = 0
        while(one_pointer<=two_pointer):
            if word[one_pointer] == word[two_pointer]:
                one_pointer += 1
                two_pointer -= 1
            else:
                if not one_more_chance:
                    if one_pointer+1<len(word) and word[one_pointer+1] == word[two_pointer]:
                        one_pointer += 1
                        one_more_chance = 1
                    elif two_pointer - 1>=0 and word[one_pointer] == word[two_pointer-1]:
                        two_pointer -= 1
                        one_more_chance = 1
                else:
                    one_more_chance = 2
                    break
    
        print(min(temp,one_more_chance))
        continue
    print(one_more_chance)