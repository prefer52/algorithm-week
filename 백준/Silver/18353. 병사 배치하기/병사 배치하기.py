n = int(input())
powers = list(map(int, input().split()))
seq = [1]*n
count = 1
for i in range(1, n):
    for j in range(i):
        if powers[j] > powers[i]:
            seq[i] = max(seq[i], seq[j] + 1)
    
print(n - max(seq))