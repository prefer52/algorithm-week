from sys import stdin
from collections import deque

r, c = map(int, stdin.readline().split())
maps = [['!'] + list(stdin.readline().rstrip()) + ['!'] for _ in range(r)]
maps = [['!']*len(maps[0])] + maps + [['!']*len(maps[0])]
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

jdeq, fdeq = deque(), deque()
for x in range(1, r+1):
    for y in range(1, c+1):
        if maps[x][y] == 'J':
            jdeq.append((x, y, 0))
        if maps[x][y] == 'F':
            fdeq.append((x,y))

while jdeq:
    new_fire_list = []
    while fdeq:
        fx, fy = fdeq.popleft()
        for dx, dy in moves:
            dx, dy = fx + dx , fy + dy
            if maps[dx][dy] in ('.', 'J'):
                maps[dx][dy] = 'F'
                new_fire_list.append((dx, dy))
    fdeq = deque(new_fire_list)
    
    new_jihoon_list = []
    while jdeq:
        jx, jy, time = jdeq.popleft()
        for dx, dy in moves:
            dx, dy = jx + dx , jy + dy
            if maps[dx][dy] == '!':
                print(time + 1)
                break
            if maps[dx][dy] == '.':
                maps[dx][dy] = 'J'
                new_jihoon_list.append((dx, dy, time+1))
        else:
            continue
        break
    else:
        jdeq = deque(new_jihoon_list)
        continue
    break
else:
    print("IMPOSSIBLE")