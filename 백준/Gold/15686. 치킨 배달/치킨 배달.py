from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for _ in range(n)]
chicken_pos, home_pos = [], []

for x in range(n):
    for y in range(n):
        if city[x][y] == 2:
            chicken_pos.append((x,y))
        if city[x][y] == 1:
            home_pos.append((x,y))

chicken_dists = []
for cx, cy in chicken_pos:
    chicken_dist = []
    for hx, hy in home_pos:
        chicken_dist.append(abs(cx-hx) + abs(cy-hy))
    chicken_dists.append(chicken_dist)

result = int(1e9)
chicken_array = range(len(chicken_pos))

for row in combinations(chicken_array, m):
    distances = [int(1e9)]*len(home_pos)
    for idx in row:
        for i, val in enumerate(chicken_dists[idx]):
            distances[i] = min(distances[i], val)
    result = min(result, sum(distances))

print(result)