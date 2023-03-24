def solution(storey):
    fm, result = [0,1,2,3,4,5,4,3,2,1], 0
    while storey // 1 > 0: result, storey = result + fm[storey%10], round(storey/10)
    return result
