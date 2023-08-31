from collections import deque

def solution(board):
    board = ['D' + row + 'D' for row in board]
    board = ['D'*len(board[0])] + board + ['D'*len(board[0])]
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]

    R_pos = tuple()
    for y, row in enumerate(board):
        if 'R' in row:
            R_pos = (row.find('R'), y, 0)
    
    queue = deque([R_pos])
    while queue:
        pos = queue.popleft()
        if board[pos[1]][pos[0]] == 'G':
            return pos[2]
        
        visited[pos[1]][pos[0]] = True
        for move in moves:
            x, y, moved = pos
            while board[y][x] != 'D':
                x += move[0]
                y += move[1]
            
            if not visited[y-move[1]][x-move[0]]:
                visited[y-move[1]][x-move[0]] = True
                queue.append((x-move[0], y-move[1], moved+1))
    return -1