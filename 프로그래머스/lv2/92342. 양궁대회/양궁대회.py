from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    score_up, score_down = range(11), range(11)[::-1]
    appeach_sum = sum([10-i for i in score_up if info[i]])
    result = []
    cwrs = combinations_with_replacement(score_up, n)
    count = (Counter(cwr) for cwr in cwrs)
    
    for cwr in count:
        appeach, lion = appeach_sum, 0
        for score in cwr:
            if cwr[score] > info[10-score]:
                lion += score
                if info[10-score] > 0:
                    appeach -= score
        if lion > appeach:
            result += [[lion-appeach, [cwr[10-i] for i in score_down]]]
    
    if not result:
        return [-1]
    else:
        return max(result)[1][::-1]