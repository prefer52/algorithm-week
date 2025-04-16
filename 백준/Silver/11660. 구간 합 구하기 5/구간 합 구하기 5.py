from sys import stdin

n, m = map(int, stdin.readline().split())
spaces = [[0]*(n+2)] + [[0] + list(map(int, stdin.readline().split())) + [0] for _ in range(n)] + [[0]*(n+2)]
for row in range(1, n+1):
    for col in range(2, n+1):
        spaces[row][col] += spaces[row][col-1]

for col in range(1, n+1):
    for row in range(2, n+1):
        spaces[row][col] += spaces[row-1][col]


for i in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(spaces[x2][y2] - spaces[x1-1][y2] - spaces[x2][y1-1] + spaces[x1-1][y1-1])