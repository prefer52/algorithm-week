from sys import stdin
from collections import deque

n = int(stdin.readline())
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    nodeA, nodeB = map(int, stdin.readline().split())
    nodes[nodeA].append(nodeB)
    nodes[nodeB].append(nodeA)
    
queue = deque([1])
parents = [0, 1] + [0]*(n-1)
while queue:
    parent = queue.popleft()
    for child in nodes[parent]:
        if parents[child] == 0:
            parents[child] = parent
            queue.append(child)

print('\n'.join(map(str, parents[2:])))