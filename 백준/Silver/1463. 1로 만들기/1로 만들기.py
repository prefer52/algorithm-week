n = int(input())
count = [int(1e9)]*(n+1)
count[0], count[1] = 0, 0

for i in range(1, n+1):
    if i % 3 == 0:
        count[i] = min(count[i//3] + 1, count[i])
    if i % 2 == 0:
        count[i] = min(count[i//2] + 1, count[i])
    count[i] = min(count[i-1] + 1, count[i])
    
print(count[n])