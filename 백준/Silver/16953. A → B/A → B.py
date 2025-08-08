a, b = map(int, input().split())

count = 1
while b > a:
    if b % 2 == 0:
        b >>= 1
    elif b % 10 == 1:
        b //= 10
    else:
        break
    count += 1
        
print(count if b == a else -1)