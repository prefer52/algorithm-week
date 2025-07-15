from sys import stdin
from collections import deque

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
m = int(stdin.readline())
childs = [[] for _ in range(n+1)]
parents = [0]*(n+1)
visited = [False]*(n+1)

while True:
    xy = stdin.readline()
    if not xy.strip():
        break
    
    x, y = map(int, xy.split())
    childs[x].append(y)
    parents[y] = x

queue = deque()
queue.append((a, 0))
while queue:
    person, chon = queue.popleft()
    if person == b:
        break
    if parents[person] and not visited[parents[person]]:
        visited[parents[person]] = True
        queue.append((parents[person], chon+1))
    if childs[person]:
        for child in childs[person]:
            if not visited[child]:
                visited[child] = True
                queue.append((child, chon+1))
                
if person == b:
    print(chon)
else:
    print(-1)