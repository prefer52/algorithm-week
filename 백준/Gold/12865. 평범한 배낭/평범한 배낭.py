from sys import stdin

n, k = map(int, stdin.readline().split())
items = [list(map(int, stdin.readline().split())) for _ in range(n)]
mem = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    for j in range(k+1):
        weight, value = items[i]
        bag_in = mem[i-1][j-weight] + value if j - weight >= 0 else 0
        not_bag_in = mem[i-1][j]
        mem[i][j] = max(bag_in, not_bag_in)


print(mem[n-1][k])