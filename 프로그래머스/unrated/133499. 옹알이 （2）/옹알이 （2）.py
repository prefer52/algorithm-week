def solution(babbling):
    word = [['a','w'],['aya','woo'],['y','m'],['ye','ma']]
    result = 0
    for i in babbling:
        j, pre_word, next = 0, '', 0
        while j < len(i):
            if (i[j] in word[0]) and (j+2 < len(i)):
                if (i[j:j+3] in word[1]) and (i[j:j+3] != pre_word): next = 3
                else: break
            elif (i[j] in word[2]) and (j+1 < len(i)):
                if (i[j:j+2] in word[3]) and (i[j:j+2] != pre_word): next = 2
                else: break
            else: break
            pre_word = i[j:j+next]
            j += next
        if j >= len(i): result += 1
    return result