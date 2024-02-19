from collections import deque

def solution(s):
    result = len(s)
    for i in range(1, len(s)//2 + 1):
        pressed_str, strs = '', deque()
        for j in range(0, len(s), i):
            strs.append(s[j:j+i])
    
        dupl, count = strs.popleft(), 1
        while strs:
            cur = strs.popleft()
            if dupl == cur:
                count += 1
            else:
                if count != 1:
                    pressed_str += str(count)
                pressed_str += dupl
                dupl, count = cur, 1
        if count != 1:
            pressed_str += str(count)
        pressed_str += dupl
        result = min(result, len(pressed_str))
        
    return result