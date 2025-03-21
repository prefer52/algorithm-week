from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
bus_infos = [list(map(int, stdin.readline().split())) for _ in range(m)]
start_city, destination_city = map(int, stdin.readline().split())

citys_info = [[] for _ in range(n+1)]
costs = [1e9]*(n+1)
for start, end, cost in bus_infos:
    citys_info[start].append((end, cost))
    
heap = []
heapq.heappush(heap, (0, start_city))
costs[start_city] = 0
while heap:
    current_cost, current_city = heapq.heappop(heap)
    if current_cost > costs[current_city]:
        continue
    
    for end_city, end_cost in citys_info[current_city]:
        if costs[end_city] > current_cost + end_cost:
            costs[end_city] = current_cost + end_cost
            heapq.heappush(heap, (costs[end_city], end_city))

print(costs[destination_city])