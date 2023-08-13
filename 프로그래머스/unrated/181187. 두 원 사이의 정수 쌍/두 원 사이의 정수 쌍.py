import math

def solution(r1, r2):
    r1_circle, r2_circle = 0, 0
    
    for x in range(1, r2):
        r2_circle += int((r2**2 - x**2)**0.5)
    r2_circle = r2_circle*4 + r2*4 + 1
    
    for x in range(1, r1):
        y = ((r1**2 - x**2)**0.5)
        if math.ceil(y-1) == int(y):
            r1_circle += int(y)
        else:
            r1_circle += int(y-1)
    r1_circle = r1_circle*4 + (r1-1)*4 + 1
    
    return r2_circle - r1_circle