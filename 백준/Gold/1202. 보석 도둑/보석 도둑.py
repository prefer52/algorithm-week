from sys import stdin
import heapq

n, k = map(int, stdin.readline().split())
jewerlys = [list(map(int, stdin.readline().split())) for _ in range(n)]
bags = [int(stdin.readline()) for _ in range(k)]

jewerlys.sort(key=lambda x: (x[0], x[1]), reverse=True)
bags.sort()
maxHeap = []
result = 0

for bag in bags:
    for i in range(len(jewerlys)):
        if jewerlys[-1][0] <= bag:
            weight, cost = jewerlys.pop()
            heapq.heappush(maxHeap, (-cost, weight))
        else:
            break
    if maxHeap:
        result += -heapq.heappop(maxHeap)[0]
    
print(result)