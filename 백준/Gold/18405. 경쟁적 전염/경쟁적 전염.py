from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
maps = [[1001] + list(map(int, stdin.readline().split())) + [1001] for _ in range(n)]
s, x, y = map(int, stdin.readline().split())
maps = [[1001]*(n+2)] + maps + [[1001]*(n+2)]
deq = deque(sorted([(nx, ny, maps[nx][ny]) for nx in range(1, n+1) for ny in range(1, n+1) if maps[nx][ny] > 0], key=lambda value: value[2]))
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while s > 0 and deq:
    new_deq = deque()
    while deq:
        nx, ny, virus = deq.popleft()
        for dx, dy in moves:
            dx, dy = nx + dx, ny + dy
            if maps[dx][dy] == 0:
                new_deq.append((dx, dy, virus))
                maps[dx][dy] = virus
    deq = deque(sorted(new_deq, key=lambda x: x[2]))
    s -= 1

print(maps[x][y])