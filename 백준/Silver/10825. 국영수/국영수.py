from sys import stdin

n = int(stdin.readline())
infos = sorted([stdin.readline().split() for _ in range(n)],
               key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
print('\n'.join(list(map(lambda x: x[0], infos))))