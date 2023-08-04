from collections import deque

def solution(order):
    box_num = 1
    sub_belt = deque()
    
    for i in range(0, len(order)): 
        for box_num in range(box_num, order[i]+1):
            sub_belt.append(box_num)
        
        if box_num == order[i]:
            box_num += 1
            sub_belt.pop()
        elif sub_belt.pop() != order[i]:
            return i
    return len(order)