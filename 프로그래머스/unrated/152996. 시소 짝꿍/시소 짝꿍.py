from collections import Counter

def solution(weights):
    result = 0
    count = Counter(weights)
    ratios = [2/3, 1/2, 3/4]
    for w in count:
        result += (count[w]*(count[w]-1))//2
        for ratio in ratios:
            if w*ratio in count:
                result += count[w]*count[w*ratio]
    
    return result