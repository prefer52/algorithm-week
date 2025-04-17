from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
users = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    if b not in users[a]:
        users[a].append(b)
        users[b].append(a)

results = []
for i in range(1, n+1):
    meet_count = [0]*(n+1)
    meet_count[i] = 0
    deq = deque()
    deq.append((i, 0))
    while deq:
        current_friend, step_count = deq.popleft()
        for friend in users[current_friend]:
            if meet_count[friend] == 0:
                meet_count[friend] = step_count + 1
                deq.append((friend, step_count + 1))
    results.append(sum(meet_count))

print(results.index(min(results)) + 1)