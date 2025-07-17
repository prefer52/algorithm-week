from sys import stdin
import heapq

n = int(stdin.readline())
m = int(stdin.readline())
heap = []
parents = [i for i in range(n+1)]

def find_parents(a):
    while a != parents[a]:
        a = parents[a]
    return a

def union_parents(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a 

for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    heapq.heappush(heap, (c, a, b))
        
result = 0
while heap:
    c, a, b = heapq.heappop(heap)
    if find_parents(a) != find_parents(b):
        union_parents(a, b)
        result += c

print(result)