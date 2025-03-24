from sys import stdin

n, m = map(int, stdin.readline().split())

map = [list(map(int, stdin.readline().split())) for _ in range(n)]

tetrominoses = [[(0, 0), (0, 1), (0, 2), (0, 3)], [(0, 0), (1, 0), (2, 0), (3, 0)],
              [(0, 0), (0, 1), (1, 0), (1, 1)],
              [(0, 0), (1, 0), (2, 0), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (-1, 2)],
              [(0, 0), (1, 0), (2, 0), (2, -1)], [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0), (0, 1)], [(0, 0), (0, 1), (0, 2), (1, 2)],
              [(0, 0), (1, 0), (1, 1), (1, 2)], [(0, 0), (0, 1), (-1, 1), (-1, 2)], [(0, 0), (-1, 0), (-1, 1), (-2, 1)], [(0, 0), (0, 1), (1, 1), (1, 2)],
              [(0, 0), (0, 1), (0, 2), (1, 1)], [(0, 0), (0, 1), (-1, 1), (1, 1)], [(0, 0), (0, 1), (-1, 1), (0, 2)], [(0, 0), (1, 0), (1, 1), (2, 0)]]

sums = []
for tetrominos in tetrominoses:
    for x in range(m):
        for y in range(n):
            sum = 0
            for dy, dx in tetrominos:
                dy, dx = y + dy, x + dx
                if 0 > dy or dy >= n or dx < 0 or dx >= m:
                    break
                sum += map[dy][dx]
            else:
                sums.append(sum)
            
print(max(sums))