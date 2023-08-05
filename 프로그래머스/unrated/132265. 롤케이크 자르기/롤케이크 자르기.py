def solution(topping):
    result = 0
    topping_type = set()
    left_bread, right_bread = [], []
    
    for i in topping:
        topping_type.add(i)
        left_bread.append(len(topping_type))
    topping_type.clear()
    
    for i in list(reversed(topping)):
        topping_type.add(i)
        right_bread.append(len(topping_type))
    right_bread.reverse()
    
    for i in range(0, len(topping)-1):
        if left_bread[i] == right_bread[i+1]:
            result += 1
            
    return result