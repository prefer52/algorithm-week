def solution(n, m, section):
    answer = 0

    section_num = len(section)
    i = 0
    while i < section_num:
        j = i+1
        while (j < section_num) and (section[j]-section[i]+1 <= m):
            j += 1
    
        answer += 1
        i = j
 
    return answer