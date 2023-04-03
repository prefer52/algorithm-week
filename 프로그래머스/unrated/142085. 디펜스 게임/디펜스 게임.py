from heapq import heappush, heappop, heapify

def solution(n, k, enemy):
    if k >= len(enemy): return len(enemy)
    else:
        min_heap = enemy[0:k]
        heapify(min_heap)
        enemy_sum, min_enemy = 0, 0
        for i in range(k, len(enemy)):
            if min_heap[0] < enemy[i]:
                min_enemy = heappop(min_heap)
                heappush(min_heap, enemy[i])
            else:
                min_enemy = enemy[i]
            enemy_sum += min_enemy
            if enemy_sum > n: return i
        return len(enemy)