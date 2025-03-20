from sys import stdin

n = int(stdin.readline())
video = [list(map(int, list(stdin.readline().strip()))) for _ in range(n)]
compress_info = [[1]*n for _ in range(n)]

compress_unit = 1
while compress_unit < n:
    for y in range(0, n, compress_unit * 2):
        for x in range(0, n, compress_unit * 2):
            check_point = [(y, x + compress_unit), (y + compress_unit, x), (y + compress_unit, x + compress_unit)]
            for cy, cx in check_point:
                if video[y][x] != video[cy][cx] or compress_info[y][x] != compress_info[cy][cx] or compress_info[y][x] != compress_unit:
                    break
            else:
                compress_info[y][x] = compress_unit*2
    
    compress_unit *= 2
    
    
def get_compressed_video(y, x, compress_unit):
    if compress_unit == 1 or compress_info[y][x] == compress_unit:
        return str(video[y][x])
    
    compress_unit //= 2
    return '(' + get_compressed_video(y, x, compress_unit) \
        + get_compressed_video(y, x + compress_unit, compress_unit) \
        + get_compressed_video(y + compress_unit, x, compress_unit) \
        + get_compressed_video(y + compress_unit, x + compress_unit, compress_unit) \
        + ')'
        
print(get_compressed_video(0, 0, n))