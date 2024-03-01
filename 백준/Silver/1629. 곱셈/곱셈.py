a, b, c = map(int, input().split())

def pow(a, base, pow_count, b, c):
    if pow_count == b:
        return base%c
    elif pow_count*2 <= b:
        return pow(a, ((base%c)*(base%c))%c, pow_count*2, b, c)
    else:
        return ((base%c) * pow(a, a, 1, b - pow_count, c)%c)%c
    
print(pow(a, a, 1, b, c))