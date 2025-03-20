from sys import stdin

n, m = map(int, stdin.readline().split())
edges = [list(map(int, stdin.readline().split())) for _ in range(m)]
nodes = [[] for _ in range(n+1)]

for start, end in edges:
    nodes[start].append(end)
    nodes[end].append(start)

count = nodes.count([]) - 1
for start in range(1, n+1):
    if not nodes[start]:
        continue
    count += 1
    stack = [start]
    while stack:
        n_start = stack.pop()
        while nodes[n_start]:
            stack.append(nodes[n_start].pop())
            

print(count)