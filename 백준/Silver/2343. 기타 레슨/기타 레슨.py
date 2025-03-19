from sys import stdin

n, m = map(int, stdin.readline().split())
videos = list(map(int, stdin.readline().split()))

start, end = max(videos), sum(videos)
min_length = end

while start <= end:
    mid = (start + end)//2
    video_sum, count = 0, 0
    for video in videos:
        video_sum += video
        if video_sum > mid:
            count += 1
            video_sum = video
    else:
        count += 1
    
    if count <= m:
        min_length = min(min_length, mid)
        end = mid - 1
    else:
        start = mid + 1
        
print(min_length)