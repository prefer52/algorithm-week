def solution(k, d):
    max_x, result = k * (d//k), 0
    for x in range(0, max_x+1, k):
        result += int((d*d-x*x)**0.5)//k+1
    return result