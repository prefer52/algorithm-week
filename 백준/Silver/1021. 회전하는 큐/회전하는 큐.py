from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
positions = list(map(int, stdin.readline().split()))
queue = deque([i for i in range(1, n+1)])
rotate = 0

for i in positions:
    count = 0
    while queue[count] != i:
        count += 1
    rotate += min(count, len(queue) - count)
    queue.rotate(-count)
    queue.popleft()

print(str(rotate))