from sys import stdin

n = int(stdin.readline())
grapes = [int(stdin.readline()) for _ in range(n)] + [0]

dp = [[0, 0] for _ in range(n+1)]
for i in range(n):
    dp[i][0] = max(dp[i-1][1], dp[i-2][1] + grapes[i-1]) + grapes[i]
    dp[i][1] = max(dp[i-1])
        
print(max(dp[n-1]))