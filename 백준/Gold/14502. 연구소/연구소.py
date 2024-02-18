from collections import deque
import copy

n, m = map(int, input().split())
map = [[1] + list(map(int, input().split())) + [1] for _ in range(n)]
map = [[1]*(m+2)] + map + [[1]*(m+2)]
safe_count, virus_positions = 0, []
result, moves = 0, [(1, 0), (-1, 0), (0, 1), (0, -1)]
safe_positions = []

for x in range(1, m+1):
    for y in range(1, n+1):
        if map[y][x] == 0:
            safe_count += 1
            safe_positions.append((x, y))
        if map[y][x] == 2:
            virus_positions.append((x, y))

def backTracking(wall_count):
    if wall_count==3:
        global result
        new_map, new_safe_count = copy.deepcopy(map), safe_count
        for x, y in virus_positions:
            deq = deque([(x, y)])
            while deq:
                nx, ny = deq.popleft()
                for dx, dy in moves:
                    nnx, nny = nx+dx, ny+dy
                    if new_map[nny][nnx] == 0:
                        deq.append((nnx, nny))
                        new_map[nny][nnx] = 2
                        new_safe_count -= 1
        result = max(result, new_safe_count)
        return
    
    for x, y in safe_positions:
        if map[y][x] == 0:
            map[y][x] = 1
            backTracking(wall_count + 1)
            map[y][x] = 0
                

backTracking(0)
if result == 0:
    print(result)
else:
    print(result - 3)