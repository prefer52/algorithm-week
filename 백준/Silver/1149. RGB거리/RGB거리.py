from sys import stdin

n = int(stdin.readline())
costs = [list(map(int, stdin.readline().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]

for i in range(n):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
    
print(min(dp[n-1]))