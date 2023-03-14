def solution(food):
    answer = ''
    
    food_num = len(food)
    
    answer = '1'*(food[1]//2*2)
    for i in range(2, food_num):
        answer = answer[:len(answer)//2] + str(i)*(food[i]//2*2) + answer[len(answer)//2:len(answer)]
    
    answer = answer[:len(answer)//2] + '0' + answer[len(answer)//2:len(answer)]
    
    return answer