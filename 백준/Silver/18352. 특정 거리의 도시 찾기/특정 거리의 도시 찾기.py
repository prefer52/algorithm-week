from sys import stdin
from collections import deque

n, m, k, x = map(int, stdin.readline().split())
ways = [[] for _ in range(n+1)]
distance = [int(1e9)]*(n+1)
for _ in range(m):
    start, end = map(int, stdin.readline().split())
    ways[start].append(end)

deq, distance[x] = deque([x]), 0
while deq:
    start = deq.popleft()
    for end in ways[start]:
        if distance[end] == int(1e9):
            distance[end] = distance[start]+1
            deq.append(end)
            
result = [str(i) for i in range(1, n+1) if distance[i] == k]
if result:
    print('\n'.join(result))
else:
    print(-1)