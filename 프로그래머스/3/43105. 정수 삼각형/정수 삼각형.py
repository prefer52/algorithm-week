def solution(triangle):
    max_len = len(triangle)
    triangle = [[-999] + row + [-999] for row in triangle]
    for y in range(1, len(triangle)):
        for x in range(1, y+2):
            triangle[y][x] += max(triangle[y-1][x-1], triangle[y-1][x])
    
    return max(triangle[-1])