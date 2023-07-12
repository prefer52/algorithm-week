from collections import deque

def solution(numbers):
    length = len(numbers)
    answer, stack = [-1]*length, deque([(1000001,-1)])
    
    for i, number in enumerate(numbers):
        while number > stack[-1][0]:
            answer[stack[-1][1]] = number
            stack.pop()
        stack.append(((number,i)))
    
    return answer