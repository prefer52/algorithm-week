def solution(elements):
    sum_set = set()
    length, elements = len(elements), elements*2
    for i in range(1, length+1):
        for j in range(length):
            sum_set.add(sum(elements[j:j+i]))
            
    return len(sum_set)