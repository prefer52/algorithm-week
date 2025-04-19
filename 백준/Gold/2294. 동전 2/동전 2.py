from sys import stdin

n, k = map(int, stdin.readline().split())
coins = sorted(list(set([int(stdin.readline()) for _ in range(n)])))
n = len(coins)
INF = int(1e9)
used = [0] + [INF]*k

for i in range(n):
    for max_coin in range(coins[i], k+1):
        used[max_coin] = min(used[max_coin - coins[i]] + 1, used[max_coin])


print(used[k] if used[k] != INF else -1)