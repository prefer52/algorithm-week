def solution(n):
    battery_use = 0
    while n > 0:
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            battery_use += 1
    
    return battery_use