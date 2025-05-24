from sys import stdin

n = int(stdin.readline())
nodes = [[] for _ in range(n+1)]
combs = int(stdin.readline())
for i in range(combs):
    a, b = map(int, stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [False]*(n+1)
result, visited[1] = 0, True
stack = [1]
while stack:
    computer = stack.pop()
    result += 1
    for node in nodes[computer]:
        if not visited[node]:
            stack.append(node)
            visited[node] = True

print(result - 1)