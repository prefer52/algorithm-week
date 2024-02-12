n = int(input())

results = [0, 1, 2] + [0]*(n-2)

for i in range(3, n+1):
    results[i] = results[i-2] + results[i-1]

print(results[n]%10007)