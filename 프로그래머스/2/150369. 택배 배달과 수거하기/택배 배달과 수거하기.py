import heapq

def solution(cap, n, deliveries, pickups):
    deliver_heap, pickup_heap = [], []
    for i in range(n):
        if deliveries[i] > 0:
            heapq.heappush(deliver_heap, (-i, deliveries[i]))
        if pickups[i] > 0:
            heapq.heappush(pickup_heap, (-i, pickups[i]))
    
    result = 0
    while deliver_heap or pickup_heap:
        max_distance = max(-deliver_heap[0][0] if deliver_heap else 0, -pickup_heap[0][0] if pickup_heap else 0) + 1
        
        for heap in (deliver_heap, pickup_heap):
            remain_cap = cap
            while heap:
                distance, cap_count = heapq.heappop(heap)
                if cap_count > remain_cap:
                    heapq.heappush(heap, (distance, cap_count-remain_cap))
                    break
                remain_cap -= cap_count
        
        result += max_distance*2
    return result