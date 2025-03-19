from sys import stdin

n = int(stdin.readline())
array_a = sorted(list(map(int, stdin.readline().split())), reverse=True)
array_b = sorted(list(map(int, stdin.readline().split())))
print(str(sum([array_a[i] * array_b[i] for i in range(n)])))