from itertools import product

def solution(places):
    result, plus = [0, 0, 0, 0, 0], [(-1,0), (0, -1), (1, 0), (0, 1)]
    X = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    
    for idx, i in enumerate(places):
        wall = [list('O'*9)]*2
        i = wall + [['O']*2 + list(j) + ['O']*2 for j in i] + wall #out of range 방지
        for x, y in product(range(2,7), repeat=2):
            if i[x][y] == 'P':
                if any([i[x+a][y+b] == 'P' for a, b in plus]): break
                if any([i[x+2*a][y+2*b] + i[x+a][y+b] == 'PO' for a, b in plus]): break
                x_str = ''.join([i[x+a][y+b] for a, b in X])
                if 'PO' in x_str or 'OP' in x_str: break
        else: result[idx] = 1
    return result
