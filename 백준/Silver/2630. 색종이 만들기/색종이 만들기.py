from sys import stdin

n = int(stdin.readline())
color_paper = [list(map(int, stdin.readline().split())) for _ in range(n)]
color_count = [0, 0]

def count_paper(x1, y1, n):
    if n == 1:
        color_count[color_paper[y1][x1]] += 1
        return
    
    init_color = color_paper[y1][x1]
    for i in range(y1, y1+n):
        for j in range(x1, x1+n):
            if color_paper[i][j] != init_color:
                n //= 2
                count_paper(x1, y1, n)
                count_paper(x1 + n, y1, n)
                count_paper(x1, y1 + n, n)
                count_paper(x1 + n, y1 + n, n)
                return
    color_count[init_color] += 1
    return
    
count_paper(0, 0, n)
print(color_count[0], color_count[1], sep="\n")