def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)):
        discount_list = discount[i:i+10]
        for j, product in enumerate(want):
            if number[j] > discount_list.count(product):
                break
        else:
            answer += 1
            
    return answer