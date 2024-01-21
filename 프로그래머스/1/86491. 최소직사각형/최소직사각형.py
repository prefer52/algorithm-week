def solution(sizes):
    maxLength = [max(pair) for pair in sizes]
    minLength = [min(pair) for pair in sizes]
    
    return max(maxLength) * max(minLength)