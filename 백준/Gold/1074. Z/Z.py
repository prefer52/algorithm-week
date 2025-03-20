n, r, c = map(int, input().split())

def visit(row, column, move, visit_count):
    if move == 1:
        if (r, c) == (row, column):
            print(visit_count)
        return
    
    move //= 2
    if row + move <= r and column + move <= c:
        visit(row + move, column + move, move, visit_count + move*move*3)
    elif r < row + move and c < column + move:
        visit(row, column, move, visit_count)
    elif r < row + move:
        visit(row, column + move, move, visit_count + move*move)
    else:
        visit(row + move, column, move, visit_count + move*move*2)

visit(0, 0, 2**n, 0)