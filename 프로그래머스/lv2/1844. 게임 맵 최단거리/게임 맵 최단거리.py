from collections import deque

way = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(maps):
    n, m = len(maps), len(maps[0])
    maps = [[0] + row + [0] for row in maps]
    maps = [[0]*(m+2)] + maps + [[0]*(m+2)]
    queue = deque([[1,1,1]])
    maps[1][1] = 0
    
    while queue:
        x, y, move = queue.popleft()
        if (x,y) == (m, n):
            return move
        else:
            for path in way:
                if maps[y+path[1]][x+path[0]] == 1:
                    queue.append([x+path[0], y+path[1], move+1])
                    maps[y+path[1]][x+path[0]] = 0
    
    return -1