from sys import stdin

k, n = map(int, stdin.readline().split())
lines = [int(stdin.readline()) for _ in range(k)]
maxLength = 0

start, end = 1, 2**31 - 1
while start <= end:
    mid = (start + end) // 2
    count = sum(list(map(lambda line: line//mid, lines)))
    if count >= n:
        maxLength = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(maxLength)