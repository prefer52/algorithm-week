from sys import stdin

n = int(stdin.readline())
triangle = [[-999] + list(map(int, stdin.readline().split())) + [-999] for i in range(n)]
for y in range(1, n):
    for x in range(1, y+2):
        triangle[y][x] += max(triangle[y-1][x-1], triangle[y-1][x])
print(max(triangle[-1]))