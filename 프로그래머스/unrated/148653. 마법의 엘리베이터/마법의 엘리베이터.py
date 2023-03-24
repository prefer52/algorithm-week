def solution(storey):
    fm, result = [0,1,2,3,4,5,4,3,2,1], 0
    while storey // 1 > 0:
        result += fm[storey%10]
        if storey%10 < 5 or (storey%10 == 5 and storey//10%10 < 5): storey //= 10
        else: storey = storey//10 + 1
    return result