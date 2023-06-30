from collections import deque
from sys import stdin

n = int(stdin.readline())
sequence = [int(stdin.readline()) for i in range(n)]
op, stack = [], deque([0])
i = 1

while i <= n or sequence:
    while i <= sequence[0]:
        stack.append(i)
        op.append('+')
        i += 1
    
    if stack[-1] != sequence[0]:
        break
    else:
        stack.pop()
        del sequence[0]
        op.append('-')

if sequence:
    print('NO')
else:
    print('\n'.join(op))