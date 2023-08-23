def solution(n):
    battery_use = 0
    while n > 0:
        battery_use += n%2
        n = n>>1 if n%2 == 0 else n-1
    return battery_use