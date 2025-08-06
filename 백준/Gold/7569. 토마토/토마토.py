from sys import stdin
from collections import deque

m, n, h = map(int, stdin.readline().split())
tomatos_tower = []
MOVES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
deq = deque()

for _ in range(h):
    tomatos = [list(map(int, stdin.readline().split())) for _ in range(n)]
    tomatos_tower.append(tomatos)
    
for x in range(m):
    for y in range(n):
        for z in range(h):
            if tomatos_tower[z][y][x] == 1:
                deq.append((x, y, z, 0))

day = 0
while deq:
    x, y, z, day = deq.popleft()
    for dx, dy, dz in MOVES:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomatos_tower[nz][ny][nx] == 0:
            tomatos_tower[nz][ny][nx] = 1
            deq.append((nx, ny, nz, day+1))

result = day
for x in range(m):
    for y in range(n):
        for z in range(h):
            if tomatos_tower[z][y][x] == 0:
                result = -1
                break

print(result)