from collections import deque

n = int(input())
k = int(input())
board = [[-1] + [0] * n + [-1] for _ in range(n)]
board = [[-1]*(n+2)] + board + [[-1]*(n+2)]
for _ in range(k):
    y, x = map(int, input().split())
    board[y][x] = 1
    
l = int(input())
actions = deque([input().split() for _ in range(l)])

moves = {'U':(0, -1), 'D':(0, 1), 'R':(1, 0), 'L':(-1, 0)}
dir_info = {('R', 'L'):'U', ('R', 'D'):'D', ('L', 'L'):'D', ('L', 'D'):'U',
            ('U', 'L'):'L', ('U', 'D'):'R', ('D', 'L'):'R', ('D', 'D'):'L',}
dir = 'R'
move = moves[dir]
worm = deque([(1, 1)])

t, r = actions.popleft()
time = 1
while True:
    x, y = worm[-1][0] + move[0], worm[-1][1] + move[1]
    if (board[y][x] == -1) or (x, y) in worm:
        break
    worm.append((x, y))
    
    if (board[y][x] == 1):
        board[y][x] = 0
    else:
        worm.popleft()
    
    if time == int(t):
        dir = dir_info[(dir, r)]
        move = moves[dir]
        if actions:
            t, r = actions.popleft()
    time += 1
        
print(time)