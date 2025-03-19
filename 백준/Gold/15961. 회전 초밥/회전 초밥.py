from sys import stdin

n, d, k, c = map(int, stdin.readline().split())
sushis = [int(stdin.readline()) for i in range(n)]

sushis += sushis[0:k-1]
current_sushi = [0]*(d+1)
current_sushi[c], max_count = 1, 1

for i in range(k):
    if current_sushi[sushis[i]] == 0:
        max_count += 1
    current_sushi[sushis[i]] += 1

current_count = max_count
for i in range(k, len(sushis)):
    if current_sushi[sushis[i]] == 0:
        current_count += 1
    current_sushi[sushis[i]] += 1
    if current_sushi[sushis[i-k]] == 1:
        current_count -= 1
    current_sushi[sushis[i-k]] -= 1
    max_count = max(current_count, max_count)
    
print(max_count)