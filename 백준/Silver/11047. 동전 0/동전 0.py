from sys import stdin

n, k = map(int, input().split())
coins = [int(stdin.readline()) for _ in range(n)][::-1]
result = 0

for coin in coins:
    result += k // coin
    k %= coin
    if k == 0:
        break
    
print(result)