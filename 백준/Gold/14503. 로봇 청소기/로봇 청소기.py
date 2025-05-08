from sys import stdin

DS = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
REVERSE_DS = {(-1, 0):0, (0, 1):1, (1, 0):2, (0, -1):3}
MOVES = list(DS.values())
n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
spaces = [list(map(int, stdin.readline().split())) for _ in range(n)]
clean_count = 0

while True:
    # 현재 칸이 청소되지 않은 경우 현재 칸을 청소한다.
    if spaces[r][c] == 0:
        spaces[r][c] = -1
        clean_count += 1
    
    for i in range(1, 5):
        dy, dx = MOVES[d - i]
        if spaces[r + dy][c + dx] == 0:
            d = REVERSE_DS[MOVES[d-i]]
            r, c = r + dy, c + dx
            break
    else:
        dy, dx = DS[d]
        r, c = r - dy, c - dx
        if spaces[r][c] == 1:
            break
        continue
    
print(clean_count)