from sys import stdin
from collections import deque

results, space = [], []
MOVES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
while True:
    w, h = map(int, stdin.readline().split())
    if (w, h) == (0, 0):
        break
    space = [[0]*(w+2)] + [[0] + list(map(int, stdin.readline().split())) + [0] for i in range(h)] + [[0]*(w+2)]
    result = 0

    for x in range(1, w+1):
        for y in range(1, h+1):
            if space[y][x] == 0:
                continue
            result += 1
            deq = deque()
            deq.append((y, x))
            
            while deq:
                ny, nx = deq.pop()
                space[ny][nx] = 0
                for dy, dx in MOVES:
                    if space[ny + dy][nx + dx] == 1:
                        deq.append((ny + dy, nx + dx))
    results.append(str(result))
    
print('\n'.join(results))