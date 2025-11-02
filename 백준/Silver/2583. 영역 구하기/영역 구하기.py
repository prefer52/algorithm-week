from sys import stdin

m, n, k = map(int, stdin.readline().split())
poses = [list(map(int, stdin.readline().split())) for _ in range(k)]
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

spaces = [[False]*(n+2)] + [[False] + [True]*n + [False] for _ in range(m)] + [[False]*(n+2)]

for lx, ly, rx, ry in poses:
    for row in range(ly + 1, ry + 1):
        for col in range(lx + 1, rx + 1):
            spaces[row][col] = False
            
result = []
for y in range(1, m+1):
    for x in range(1, n+1):
        if not spaces[y][x]:
            continue
        
        area = 0
        stack = [(x, y)]
        spaces[y][x] = False
        while stack:
            px, py = stack.pop()
            area += 1
            for dx, dy in MOVES:
                nx, ny = px + dx, py + dy
                if spaces[ny][nx]:
                    stack.append((nx, ny))
                    spaces[ny][nx] = False
        result.append(area)
        
print(len(result))
print(' '.join(map(str, sorted(result))))