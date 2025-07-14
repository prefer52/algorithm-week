from sys import stdin

n, m = map(int, stdin.readline().split())
times = [int(stdin.readline()) for _ in range(n)]

start, end = 1, max(times)*m
while start <= end:
    mid = (start + end)//2
    total = sum([mid//time for time in times])
    if total < m:
        start = mid + 1
    else:
        end = mid - 1
        
print(start)