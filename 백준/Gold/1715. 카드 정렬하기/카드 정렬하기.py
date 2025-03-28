from sys import stdin
import heapq

n = int(stdin.readline())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(stdin.readline()))

result = 0
if n == 1:
    print(0)
else:
    while True:
        if len(heap) == 1:
            print(result)
            break
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        result += first + second
        heapq.heappush(heap, first+second)