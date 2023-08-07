from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    appeach_sum = 0
    result = []
    for i in range(11):
        if info[i]:
            appeach_sum += 10-i
    cwrs = combinations_with_replacement(range(11), n)
    cwrs_counter = ((Counter(cwr) for cwr in cwrs))
    
    for cwr in cwrs_counter:
        appeach_score = appeach_sum
        lion_score = 0
        for score in cwr:
            if cwr[score] > info[10-score]:
                lion_score += score
                if info[10-score] > 0:
                    appeach_score -= score
        if lion_score > appeach_score:
            result.extend([[lion_score-appeach_score, [cwr[10-i] for i in range(11)]]])
    if not result:
        return [-1]
    else:
        result.sort(key=lambda x:-x[0])
        return result[0][1]