from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
tomatos_tower = [[[-1]*(m+2) for _ in range(n+2)]]
MOVES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
deq = deque()

for _ in range(h):
    tomatos = [[-1]*(m+2)] + [[-1] + list(map(int, stdin.readline().split())) + [-1] for _ in range(n)] + [[-1]*(m+2)]
    tomatos_tower.append(tomatos)
tomatos_tower.append([[-1]*(m+2) for _ in range(n+2)])
    
for x in range(1, m+1):
    for y in range(1, n+1):
        for z in range(1, h+1):
            if tomatos_tower[z][y][x] == 1:
                deq.append((x, y, z, 0))

day = 0
while deq:
    x, y, z, day = deq.popleft()
    for dx, dy, dz in MOVES:
        nx, ny, nz = x + dx, y + dy, z + dz
        if tomatos_tower[nz][ny][nx] == 0:
            tomatos_tower[nz][ny][nx] = 1
            deq.append((nx, ny, nz, day+1))

result = day
for x in range(1, m+1):
    for y in range(1, n+1):
        for z in range(1, h+1):
            if tomatos_tower[z][y][x] == 0:
                result = -1
                break

print(result)