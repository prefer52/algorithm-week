def solution(dartResult):
    scores, turn, bonus = [0, 0, 0], 0, {'S':1, 'D':2, 'T':3}
    i = 0
    
    while i < len(dartResult):
        num_string = ''
        for j in range(i, len(dartResult)):
            if not dartResult[j].isdecimal():
                break
            num_string += dartResult[j]
            
        num, i = int(num_string)**bonus[dartResult[j]], j+1
        scores[turn] = num
        if i < len(dartResult) and not dartResult[i].isdecimal():
            scores[turn] = scores[turn]*2 if dartResult[i] == '*' else -scores[turn]
            if turn > 0:
                scores[turn-1] = scores[turn-1]*2 if dartResult[i] == '*' else scores[turn-1]
            i += 1
        
        turn += 1
    
    return sum(scores)
            