from sys import stdin
import math

n = int(stdin.readline())
is_prime = [False, False] + [True]*(n-1)

for i in range(2, int(math.sqrt(n)) + 1):
    for j in range(2, n // i + 1):
        is_prime[i*j] = False

prime_numbers = [i for i in range(n+1) if is_prime[i]]
prime_numbers_len = len(prime_numbers)
start, end, total, count = 0, 0, 0, 0

while start <= end:
    if total < n:
        if end == prime_numbers_len:
            break
        total += prime_numbers[end]
        end += 1
    elif total >= n:
        total -= prime_numbers[start]
        start += 1
        
    if total == n:
        count += 1

print(count)