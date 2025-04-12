from sys import stdin

n, m, y, x, k = map(int, stdin.readline().split())
spaces = [[-1] * (m+2)] + [[-1] + list(map(int, stdin.readline().split())) + [-1] for _ in range(n)] + [[-1] * (m+2)]
moves = stdin.readline().split()
MOVE = {'1':(0, 1), '2':(0, -1), '3':(-1, 0), '4':(1, 0)}
dice = {'U':0, 'D':0, 'R':0, 'L':0, 'C':0, 'F':0} # C는 Ceil, F는 Floor

def move(mv):
    if mv == '1':
        dice['C'], dice['R'], dice['F'], dice['L'] = dice['L'], dice['C'], dice['R'], dice['F']
    elif mv == '2':
        dice['C'], dice['R'], dice['F'], dice['L'] = dice['R'], dice['F'], dice['L'], dice['C']
    elif mv == '3':
        dice['C'], dice['U'], dice['F'], dice['D'] = dice['D'], dice['C'], dice['U'], dice['F']
    else:
        dice['C'], dice['U'], dice['F'], dice['D'] = dice['U'], dice['F'], dice['D'], dice['C']

result = []
y, x = y + 1, x + 1
for mv in moves:
    dy, dx = MOVE[mv]
    if spaces[dy + y][dx + x] == -1:
        continue
    
    y, x = y + dy, x + dx
    move(mv)
    if spaces[y][x]:
        dice['F'] = spaces[y][x]
        spaces[y][x] = 0
    else:
        spaces[y][x] = dice['F']
    result.append(str(dice['C']))
    
print('\n'.join(result))