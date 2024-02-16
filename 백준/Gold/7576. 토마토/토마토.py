from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
box = [[-1] + list(map(int, stdin.readline().split())) + [-1] for _ in range(n)]
box = [[-1]*(m+2)] + box + [[-1]*(m+2)]
deq = deque([(x, y) for x in range(m+1) for y in range(n + 1) if box[y][x] == 1])
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while deq:
    x, y = deq.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if box[ny][nx] == 0:
            deq.append((nx, ny))
            box[ny][nx] = box[y][x] + 1

minDay = 0
for row in box:
    if 0 in row:
        print(-1)
        break
    minDay = max(minDay, max(row))
else:
    print(minDay-1)