def solution(sizes):
    return max(max(pair) for pair in sizes) * max(min(pair) for pair in sizes)