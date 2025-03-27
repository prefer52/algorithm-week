from sys import stdin

t = int(stdin.readline())
result = []
for _ in range(t):
    m, n, k = map(int, stdin.readline().split())
    poses = [list(map(int, stdin.readline().split())) for _ in range(k)]
    maps = [[0]*(m+2) for _ in range(n+2)]
    MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for x, y in poses:
        maps[y+1][x+1] = 1
    count = 0

    for x in range(1, m+1):
        for y in range(1, n+1):
            if maps[y][x] == 0:
                continue
            count += 1
            stack = []
            stack.append((y, x))
            while stack:
                ny, nx = stack.pop()
                maps[ny][nx] = 0
                for dy, dx in MOVE:
                    dy, dx = ny + dy, nx + dx
                    if maps[dy][dx] == 1:
                        stack.append((dy, dx))

    result.append(str(count))
    
print('\n'.join(result))