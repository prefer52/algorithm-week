from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
pictures = [[0] + list(map(int, stdin.readline().split())) + [0] for _ in range(n)]
pictures = [[0]*len(pictures[0])] + pictures + [[0]*len(pictures[0])]
deq, moves = deque(), [(1, 0), (-1, 0), (0, 1), (0, -1)]
picture_count, max_area = 0, 0

for x in range(1, n+1):
    for y in range(1, m+1):
        if pictures[x][y]:
            picture_count += 1
            deq.append((x, y))
            pictures[x][y], area = 0, 0
            while deq:
                nx, ny = deq.popleft()
                area += 1
                for dx, dy in moves:
                    dx, dy = nx + dx, ny + dy
                    if pictures[dx][dy]:
                        deq.append((dx,dy))
                        pictures[dx][dy] = 0
            max_area = max(max_area, area)

print(picture_count)
print(max_area)