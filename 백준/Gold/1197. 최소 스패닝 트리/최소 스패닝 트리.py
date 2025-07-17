from sys import stdin
import heapq

v, e = map(int, stdin.readline().split())
heap = []
parents = [i for i in range(v + 1)]
for i in range(e):
    a, b, c = map(int, stdin.readline().split())
    heapq.heappush(heap, (c, a, b))

def find_parent(a):
    while a != parents[a]:
        a = parents[a]
    return a

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
        
result = 0
while heap:
    c, a, b = heapq.heappop(heap)
    if find_parent(a) != find_parent(b):
        union(a, b)
        result += c
        
print(result)