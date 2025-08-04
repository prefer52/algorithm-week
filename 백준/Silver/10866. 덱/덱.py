from collections import deque
from sys import stdin

n = int(stdin.readline())
instructions = [stdin.readline().strip().split() for _ in range(n)]
deq = deque()

for instruction in instructions:
    operation = instruction[0]
    if len(instruction) == 2:
        operand = instruction[1]
    
    if operation == 'push_front':
        deq.appendleft(operand)
    elif operation == 'push_back':
        deq.append(operand)
    elif operation == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif operation == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif operation == 'size':
        print(len(deq))
    elif operation == 'empty':
        print('0' if deq else '1')
    elif operation == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif operation == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)