from sys import stdin

n = int(stdin.readline())
spaces = [[0]*(n+2)] + [[0] + list(map(int, stdin.readline().split())) + [0] for _ in range(n)] + [[0]*(n+2)]
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

max_zone_count = 1
for height in range(1, 101):
    zone_count = 0
    visited = [[False]*(n+2) for _ in range(n+2)]
    for y in range(1, n+1):
        for x in range(1, n+1):
            if spaces[y][x] <= height or visited[y][x]:
                continue
            
            zone_count += 1
            visited[y][x] = True
            stack = [(x, y)]
            while stack:
                px, py = stack.pop()
                for dx, dy in MOVES:
                    nx, ny = px + dx, py + dy
                    if spaces[ny][nx] > height and not visited[ny][nx]:
                        stack.append((nx, ny))
                        visited[ny][nx] = True
                        
    max_zone_count = max(max_zone_count, zone_count)

print(max_zone_count)