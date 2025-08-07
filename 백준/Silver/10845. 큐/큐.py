from sys import stdin
from collections import deque

n = int(stdin.readline())
instructions = [stdin.readline().split() for _ in range(n)]
queue = deque()

for instruction in instructions:
    if instruction[0] == 'push':
        queue.append(instruction[1])
    elif instruction[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        print(0 if queue else 1)
    elif instruction[0] == 'front':
        print(queue[0] if queue else -1)
    elif instruction[0] == 'back':
        print(queue[-1] if queue else -1)