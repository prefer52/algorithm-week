from sys import stdin
import heapq

INF = int(1e9)
v, e = map(int, stdin.readline().split())
k = int(stdin.readline())
edges = [[] for _ in range(v+1)]
distances = [INF] * (v+1)

for i in range(e):
    start, end, distance = map(int, stdin.readline().split())
    edges[start].append((end, distance))

minHeap, distances[k] = [], 0
heapq.heappush(minHeap, (0, k))
while minHeap:
    distance, node = heapq.heappop(minHeap)

    if distances[node] < distance:
        continue
    
    for nodeInfo in edges[node]:
        cost = nodeInfo[1] + distance
        if cost < distances[nodeInfo[0]]:
            distances[nodeInfo[0]] = cost
            heapq.heappush(minHeap, (cost, nodeInfo[0]))

results = ''
for i in range(1, v+1):
    results += (str(distances[i]) if distances[i] != INF else 'INF') + '\n'
print(results)