from sys import stdin

n = int(stdin.readline())
table = [list(map(int, stdin.readline().split())) for _ in range(n)]
for i in range(len(table)):
    if table[i][0] + i - 1 >= n:
        table[i][1] = 0

for i in range(n-1, -1, -1):
    day, money = table[i]
    if money and i + day < n:
        table[i][1] += max(list(zip(*table[i+day:]))[1])

print(max(list(zip(*table))[1]))