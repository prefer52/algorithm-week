from math import gcd

def solution(arrayA, arrayB):
    gcdA, gcdB = arrayA[0], arrayB[0]
    for i in arrayA:
        gcdA = gcd(gcdA, i)
    for i in arrayB:
        gcdB = gcd(gcdB, i)
        
    if gcdA == gcdB == 1:
        return 0
    else:
        max_value, undivide_array = gcdA, arrayB
        if gcdA < gcdB:
            max_value = gcdB
            undivide_array = arrayA
            
        for i in undivide_array:
            if i % max_value == 0:
                return 0
        else:
            return max_value