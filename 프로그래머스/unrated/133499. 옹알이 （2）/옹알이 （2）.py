def solution(babbling):
    result = 0
    for i in babbling:
        j = 0
        pre_word = ''
        while j < len(i):
            if (i[j] == 'a' or i[j] == 'w') and (j+2 < len(i)):
                if (i[j:j+3] == 'aya' or i[j:j+3] == 'woo') and (i[j:j+3] != pre_word): j += 3
                else: break
                pre_word = i[j-3:j]
            elif (i[j] == 'y' or i[j] == 'm') and (j+1 < len(i)):
                if (i[j:j+2] == 'ye' or i[j:j+2] == 'ma') and (i[j:j+2] != pre_word): j+= 2
                else: break
                pre_word = i[j-2:j]
            else:
                break
        if j >= len(i): result += 1
    
    return result