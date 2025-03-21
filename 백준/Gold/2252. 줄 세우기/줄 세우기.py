from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
compares = [list(map(int, stdin.readline().split())) for _ in range(m)]
deq = deque()

indegree = [0]*(n+1)
compare_info = [[] for _ in range(n+1)]

for front, rear in compares:
    indegree[rear] += 1
    compare_info[front].append(rear)
    
for i in range(1, n+1):
    if indegree[i] == 0:
        deq.append(i)

result = []
while deq:
    front = deq.popleft()
    result.append(str(front))
    for rear in compare_info[front]:
        indegree[rear] -= 1
        if indegree[rear] == 0:
            deq.append(rear)
            
print(' '.join(result))