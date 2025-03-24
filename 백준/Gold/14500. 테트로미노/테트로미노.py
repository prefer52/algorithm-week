from sys import stdin

n, m = map(int, stdin.readline().split())

map = [[0]*(m+6) for _ in range(3)] + [[0, 0, 0] + list(map(int, stdin.readline().split())) + [0, 0, 0] for _ in range(n) ] + [[0]*(m+6) for _ in range(3)]

tetrominoses = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],
              [(0, 1), (1, 0), (1, 1)],
              [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (-1, 2)],
              [(1, 0), (2, 0), (2, -1)], [(1, 0), (1, 1), (2, 1)], [(1, 0), (2, 0), (0, 1)], [(0, 1), (0, 2), (1, 2)],
              [(1, 0), (1, 1), (1, 2)], [(0, 1), (-1, 1), (-1, 2)], [(-1, 0), (-1, 1), (-2, 1)], [(0, 1), (1, 1), (1, 2)],
              [(0, 1), (0, 2), (1, 1)], [(0, 1), (-1, 1), (1, 1)], [(0, 1), (-1, 1), (0, 2)], [(1, 0), (1, 1), (2, 0)]]

max_sum = 0
for tetrominos in tetrominoses:
    for x in range(3, m + 3):
        for y in range(3, n + 3):
            sum = map[y][x]
            for dy, dx in tetrominos:
                dy, dx = y + dy, x + dx
                sum += map[dy][dx]
            max_sum = max(max_sum ,sum)
            
print(max_sum)