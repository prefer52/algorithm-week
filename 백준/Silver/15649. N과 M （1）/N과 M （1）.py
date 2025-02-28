from sys import stdin
from itertools import permutations

n, m = map(int, stdin.readline().split())

results = sorted(list(permutations(list(map(str, range(1, n + 1))), m)))
print('\n'.join([' '.join(result) for result in results]))