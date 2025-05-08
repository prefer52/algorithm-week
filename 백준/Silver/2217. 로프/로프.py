from sys import stdin

n = int(stdin.readline())
ropes = sorted([int(stdin.readline()) for _ in range(n)])
max_weight = 0
for count, rope in enumerate(ropes):
    max_weight = max(rope*(n-count), max_weight)
    
print(max_weight)