from sys import stdin

n = int(stdin.readline())
paper = [list(map(int, stdin.readline().split())) for _ in range(n)]

def split_paper(paper, x, y, area, result):
    if area == 1:
        result[paper[y][x]] += 1
        return
    
    start = paper[y][x]
    i, j = 0, 0
    for i in range(y, y+area):
        for j in range(x, x+area):
            if paper[i][j] != start:
                area //= 3
                split_paper(paper, x, y, area, result)
                split_paper(paper, x+area, y, area, result)
                split_paper(paper, x+(area*2), y, area, result)
                
                split_paper(paper, x, y + area, area, result)
                split_paper(paper, x+area, y + area, area, result)
                split_paper(paper, x+(area*2), y + area, area, result)

                split_paper(paper, x, y + (area*2), area, result)
                split_paper(paper, x+area, y + (area*2), area, result)
                split_paper(paper, x+(area*2), y + (area*2), area, result)
                return
            
    result[paper[y][x]] += 1
        
result = [0, 0, 0]
split_paper(paper, 0, 0, n, result)
print(result[-1], result[0], result[1], sep="\n")