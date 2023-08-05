def solution(topping):
    result = 0
    left_set, right_set = set(), set()
    left_bread, right_bread = [], []
    for i in topping:
        left_set.add(i)
        left_bread.append(len(left_set))
    for i in list(reversed(topping)):
        right_set.add(i)
        right_bread.append(len(right_set))
    right_bread.reverse()
    for i in range(0, len(topping)-1):
        if left_bread[i] == right_bread[i+1]:
            result += 1
            
    return result