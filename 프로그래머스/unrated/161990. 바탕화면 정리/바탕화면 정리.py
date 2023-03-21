def find_file(wall, start, end, step):
    for i in range(start, end, step):
        if '#' in wall[i]: return i

def solution(wallpaper):
    col = list(zip(*wallpaper))
    lux = find_file(wallpaper, 0, len(wallpaper), 1)
    rdx = find_file(wallpaper, len(wallpaper)-1, -1, -1) + 1
    luy = find_file(col, 0, len(col), 1)
    rdy = find_file(col, len(col)-1, -1, -1) + 1        
    return [lux, luy, rdx, rdy]
