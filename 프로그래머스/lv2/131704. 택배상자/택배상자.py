from collections import deque

def solution(order):
    box_num = 1
    sub_belt = deque()
    
    for i in range(0, len(order)): 
        while box_num < order[i]:
            sub_belt.append(box_num)
            box_num += 1
        
        if box_num == order[i]:
            box_num += 1
        elif sub_belt.pop() != order[i]:
            return i
    return len(order)