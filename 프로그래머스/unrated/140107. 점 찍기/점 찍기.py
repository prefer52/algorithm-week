def solution(k, d):
    max_x = k * (d//k)
    result = [int((d*d-x*x)**0.5)//k for x in range(0, max_x+1, k)]
    return sum(result) + (max_x//k + 1)