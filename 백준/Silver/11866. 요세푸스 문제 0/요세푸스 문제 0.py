from sys import stdin

n, k = tuple(map(int, stdin.readline().split()))
circle = [str(i) for i in range(1, n+1)]
result = []
index = 0

while circle:
    index = (index + k - 1)%len(circle)
    result += [circle[index]]
    del circle[index]

print('<' + ', '.join(result) + '>')