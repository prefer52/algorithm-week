from collections import deque
from itertools import product

def solution(maps):
    deq, result = deque(), []
    days, plus = 0, [(-1,0), (-0, -1), (1, 0), (0, 1)]
    maps = [list(map(int, list(i.replace('X', '0')))) for i in maps]
    sea = [[0]*(len(maps[0])+2)]
    maps = sea + [[0] + i + [0] for i in maps] + sea
    
    for i, j in product(range(1, len(maps)), range(1, len(maps[0]))):
            if maps[i][j] > 0:
                deq.append((i,j))
                result.append(maps[i][j])
                while deq:
                    x, y = deq.pop()
                    days += maps[x][y]
                    maps[x][y] = 0
                    for a, b in plus:
                        if maps[x+a][y+b] > 0: deq.append((x+a, y+b))
                result[-1] = days
                days = 0
    
    if len(result) == 0: return [-1]
    else: return sorted(result)