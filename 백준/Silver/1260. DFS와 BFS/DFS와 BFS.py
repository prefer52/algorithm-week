from sys import stdin
from collections import deque

n, m, v = map(int, stdin.readline().split())
nodes = [list() for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

def dfs(start):
    stack = [start]
    result = []
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        result += [str(node)]
        for n in sorted(nodes[node], reverse=True):
            if not visited[n]:
                stack.append(n)
    return ' '.join(result) + '\n'
   
def bfs(start):
    deq = deque([start])
    visited[start] = True
    result = []
    while deq:
        node = deq.popleft()
        result += [str(node)]
        for n in sorted(nodes[node]):
            if not visited[n]:
                deq.append(n)
                visited[n] = True
    return ' '.join(result) + '\n'

result = dfs(v)
visited = [False] * (n+1)
result += bfs(v)
print(result)