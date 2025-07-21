from sys import stdin

n, d, k, c = map(int, stdin.readline().split())
sushis = [c] + [int(stdin.readline()) for _ in range(n)]
sushis += sushis[1:k]
cur_sushis, cur_sushi_set = [0]*(d+1), set(sushis[:k+1])
for i in range(k+1):
    cur_sushis[sushis[i]] += 1
max_result = len(cur_sushi_set)

for i in range(k+1, len(sushis)):
    cur_sushis[sushis[i-k]] -= 1
    if cur_sushis[sushis[i-k]] == 0:
        cur_sushi_set.remove(sushis[i-k])
    cur_sushis[sushis[i]] += 1
    cur_sushi_set.add(sushis[i])
    max_result = max(len(cur_sushi_set), max_result)
    
print(max_result)