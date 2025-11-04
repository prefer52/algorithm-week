import heapq

x = int(input())

stick = 64
heap = []
heapq.heappush(heap, stick)

while sum(heap) != x:
    shortest_stick = heapq.heappop(heap)
    half_stick = shortest_stick//2
    if sum(heap) + half_stick >= x:
        heapq.heappush(heap, half_stick)
    else:
        heapq.heappush(heap, half_stick)
        heapq.heappush(heap, half_stick)
        
print(len(heap))