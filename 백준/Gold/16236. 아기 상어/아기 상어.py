from sys import stdin
from collections import deque

n = int(stdin.readline())
spaces = [[100] * (n+2)] + [[100] + list(map(int, stdin.readline().split())) + [100] for _ in range(n)] + [[100] * (n+2)]
MOVES = [(-1, 0), (0, -1), (0, 1), (1, 0)]

for y, row in enumerate(spaces):
    if 9 in row:
        shark_pos = (y, row.index(9), 0)
        spaces[shark_pos[0]][shark_pos[1]] = 0
        break

shark_level, eating_count = 2, 0
deq = deque()
visited = [[False] * (n+2) for _ in range(n+2)]

while True:
    visited[shark_pos[0]][shark_pos[1]] = True
    deq.append(shark_pos)
    eating_list = []
    while deq:
        y, x, second = deq.popleft()
        second += 1
        for dy, dx in MOVES:
            dy, dx = dy + y, dx + x
            if not visited[dy][dx]:
                if 0 < spaces[dy][dx] < shark_level: # 잡아먹을 수 있는게 있다면
                    eating_list.append((dy, dx, second))
                    visited[dy][dx] = True
                elif spaces[dy][dx] in (shark_level, 0): # 지나갈 수 있다면
                    visited[dy][dx] = True
                    deq.append((dy, dx, second))
    if not eating_list:
        break
    eating_list.sort(key=lambda pos: (pos[2], pos[0], pos[1]))
    cur_y, cur_x, second = eating_list[0]
    shark_pos = (cur_y, cur_x, second)
    eating_count += 1
    spaces[cur_y][cur_x] = 0
    deq.clear()
    if eating_count == shark_level:
        shark_level += 1
        eating_count = 0
    visited = [[False] * (n+2) for _ in range(n+2)]
    eating_list.clear()
    

            
print(shark_pos[2])