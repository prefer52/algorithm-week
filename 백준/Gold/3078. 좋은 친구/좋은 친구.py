from sys import stdin
from collections import deque

n, k = map(int, stdin.readline().split())
names = [stdin.readline().strip() for _ in range(n)] + [['N'] * k]
names_count, good_friends = [0]*21, 0
window = deque([names[0]])
names_count[len(names[0])] += 1
for i in range(1, k+1):
    if names_count[len(names[i])]:
        good_friends += names_count[len(names[i])]
    names_count[len(names[i])] += 1
    window.append(names[i])

for i in range(k+1, n):
    names_count[len(window.popleft())] -= 1
    if names_count[len(names[i])]:
        good_friends += names_count[len(names[i])]
    names_count[len(names[i])] += 1
    window.append(names[i])

print(good_friends)