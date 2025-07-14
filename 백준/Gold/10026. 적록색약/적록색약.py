from sys import stdin

n = int(stdin.readline())
spaces = [' '*(n+2)] + [' ' + stdin.readline() + ' ' for _ in range(n)] + [' '*(n+2)]
visited = [[True]*(n+2)] + [[True] + [False]*n + [True] for _ in range(n)] + [[True]*(n+2)]
combine_visited = [[True]*(n+2)] + [[True] + [False]*n + [True] for _ in range(n)] + [[True]*(n+2)]
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

normal, combined = 0, 0
stack = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if not visited[i][j]:
            stack.append((i, j))
            visited[i][j] = True
            normal += 1
            while stack:
                y, x = stack.pop()
                for dy, dx in MOVES:
                    ny, nx = y + dy, x + dx
                    if not visited[ny][nx] and spaces[ny][nx] == spaces[y][x]:
                        stack.append((ny, nx))
                        visited[ny][nx] = True

        if not combine_visited[i][j]:
            stack.append((i, j))
            combine_visited[i][j] = True
            combined += 1
            while stack:
                y, x = stack.pop()
                for dy, dx in MOVES:
                    ny, nx = y + dy, x + dx
                    if not combine_visited[ny][nx] and (spaces[ny][nx] == spaces[y][x] or 'B' not in (spaces[ny][nx], spaces[y][x])):
                        stack.append((ny, nx))        
                        combine_visited[ny][nx] = True


print(normal, combined)