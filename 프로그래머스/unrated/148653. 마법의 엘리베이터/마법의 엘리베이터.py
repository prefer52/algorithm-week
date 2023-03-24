def solution(storey):
    fm, result = [0,1,2,3,4,5,4,3,2,1], 0
    while storey // 10 > 0:
        result += fm[storey%10]
        storey = round(storey/10)
    return result + fm[storey] + fm[round(storey/10)]