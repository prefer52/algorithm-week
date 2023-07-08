from collections import deque

def solution(s):
    length, stack = len(s), deque()
    s *= 2
    pair = {'(':')', '{':'}', '[':']'}
    result = 0
    
    for i in range(length):
        for j in range(i, length+i):
            if s[j] in ['(', '{', '[']:
                stack.append(s[j])
            elif not stack or pair[stack.pop()] != s[j]:
                break
        else:
            if not stack:
                result += 1
        stack.clear()
                
    return result