from itertools import product

def solution(places):
    result, plus = [1, 1, 1, 1, 1], [(-1,0), (0, -1), (1, 0), (0, 1)]
    X = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    
    for idx, i in enumerate(places):
        wall = [list('O'*9)]*2
        i = wall + [['O']*2 + list(j) + ['O']*2 for j in i] + wall #out of range 방지
        for x, y in product(range(2,7), repeat=2):
            if i[x][y] == 'P':
                violate = any([i[x+a][y+b] == 'P' for a, b in plus])
                violate = violate or any([i[x+2*a][y+2*b] + i[x+a][y+b] == 'PO' for a, b in plus])
                x_str = ''.join([i[x+a][y+b] for a, b in X])
                violate = violate or ('PO' in x_str or 'OP' in x_str)
                if violate:
                    result[idx] = 0
                    break
    return result