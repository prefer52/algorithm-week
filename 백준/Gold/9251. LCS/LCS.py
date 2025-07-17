a = input().strip()
b = input().strip()

dp = [[0] + [0]*len(a) for _ in range(len(b) + 1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        dp[i][j] = dp[i-1][j-1] + 1 if a[j-1] == b[i-1] else max(dp[i-1][j], dp[i][j-1])
            
            
print(dp[len(b)][len(a)])