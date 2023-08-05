def solution(topping):
    result = 0
    topping_set = set()
    left_bread, right_bread = [], []
    for i in topping:
        topping_set.add(i)
        left_bread.append(len(topping_set))
    topping_set.clear()
    for i in list(reversed(topping)):
        topping_set.add(i)
        right_bread.append(len(topping_set))
    right_bread.reverse()
    for i in range(0, len(topping)-1):
        if left_bread[i] == right_bread[i+1]:
            result += 1
            
    return result