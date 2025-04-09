from sys import stdin

n, c = map(int, stdin.readline().split())
poses = sorted([int(stdin.readline()) for _ in range(n)])

start, end = 1, poses[-1] - poses[0]
max_distance = 0

while start <= end:
    mid = (start + end) // 2 # 공유기 사이의 최소 거리
    count, pos = 1, poses[0]
    for i in range(1, n):
        if poses[i] - pos >= mid:
            count += 1
            pos = poses[i]
    
    if count >= c:
        start = mid + 1
        max_distance = max(max_distance, mid)
    elif count < c:
        end = mid - 1
    

print(max_distance)