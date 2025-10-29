from sys import stdin

n, m = map(int, stdin.readline().split())
arrays = [[0]*(m+2)] + [[0] + list(map(int, stdin.readline().split())) + [0] for _ in range(n)]
for i in range(1, n+1):
    for j in range(1, m+1):
        arrays[i][j] += arrays[i][j-1]
    for j in range(1, m+1):
        arrays[i][j] += arrays[i-1][j]
        

k = int(stdin.readline())
for _ in range(k):
    i, j, x, y = map(int, stdin.readline().split())
    print(arrays[x][y] - arrays[i-1][y] - arrays[x][j-1] + arrays[i-1][j-1])