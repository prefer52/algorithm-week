def solution(number, limit, power):
    answer = 0
        
    nList = [[i, 2] for i in range(1, number+1)]
    nList[0][1] = 1
        
    for i in range(2, number):
        j = i*2
        while(j <= number):
            nList[j - 1][1] += 1
            j += i
        
    for i in range(number):
        answer += power if nList[i][1] > limit else nList[i][1]


    return answer