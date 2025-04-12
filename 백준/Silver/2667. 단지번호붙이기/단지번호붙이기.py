from sys import stdin

ADJS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
n = int(stdin.readline())
spaces = [[0] * (n+2)] + [[0] + list(map(int, list(stdin.readline().strip()))) + [0] for _ in range(n)] + [[0] * (n+2)]
danji = []

for y in range(1, n + 1):
    for x in range(1, n + 1):
        if not spaces[y][x]:
            continue
        stack = [(y, x)]
        spaces[y][x], count = 0, 0
        
        while stack:
            ny, nx = stack.pop()
            count += 1
            for dy, dx in ADJS:
                ndy, ndx = ny + dy, nx + dx
                if spaces[ndy][ndx]:
                    spaces[ndy][ndx] = 0
                    stack.append((ndy, ndx))
        danji.append(count)

if danji:
    print(len(danji), '\n'.join(map(str, sorted(danji))), sep='\n')
else:
    print(0)