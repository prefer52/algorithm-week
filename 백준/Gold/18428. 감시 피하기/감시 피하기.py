def isInSight(x, y, move, maps):
    dx, dy = move
    while maps[x][y] != 'O':
        x, y = x + dx, y + dy
        if maps[x][y] == 'S':
            return True
    return False


def backTracking(maps, obj, teacher_positions):
    if obj == 3:
        for x, y in teacher_positions:
            if (isInSight(x, y, (1, 0), maps) or isInSight(x, y, (-1, 0), maps)
                or isInSight(x, y, (0, 1), maps) or isInSight(x, y, (0, -1), maps)):
                return False
        return True
    
    for x in range(1, n+1):
        for y in range(1, n+1):
            if maps[x][y] in ('T', 'S', 'O'):
                continue
            maps[x][y] = 'O'
            if backTracking(maps, obj+1, teacher_positions):
                return True
            maps[x][y] = 'X'
    return False
            

n = int(input())
maps = [['O'] + input().split() + ['O'] for _ in range(n)]
maps = [['O']*(n + 2)] + maps + [['O']*(n + 2)]
teacher_positions = []

for x in range(1, n+1):
    for y in range(1, n+1):
        if maps[x][y] == 'T':
            teacher_positions.append((x, y))

if backTracking(maps, 0, teacher_positions):
    print('YES')
else:
    print('NO')