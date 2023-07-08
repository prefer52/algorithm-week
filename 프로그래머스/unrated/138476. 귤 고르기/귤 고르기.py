from collections import Counter

def solution(k, tangerine):
    count_size = dict(Counter(tangerine))
    count_size = list(count_size.items())
    count_size.sort(key=lambda x:x[1], reverse=True)
    
    for count, size_tuple in enumerate(count_size):
        k -= size_tuple[1]
        if k <= 0:
            return count + 1
    
    return len(count_size)