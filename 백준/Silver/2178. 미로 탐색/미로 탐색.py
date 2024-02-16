from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
map = [[0] + list(map(int, stdin.readline().rstrip())) + [0] for _ in range(n)]
map = [[0]*(m+2)] + map + [[0]*(m+2)]

deq = deque([(1, 1)])
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while deq:
    y, x = deq.popleft()
    if (y, x) == (n, m):
        break
    
    for dy, dx in moves:
        if map[y + dy][x + dx] == 1:
            deq.append((y+dy, x+dx))
            map[y+dy][x+dx] = map[y][x] + 1
            
print(map[n][m])