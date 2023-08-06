from collections import deque
from sys import stdin

n = int(stdin.readline())
deq = deque()
result = []
for i in range(n):
    op = stdin.readline().strip()
    if op.startswith('1'):
        deq.appendleft(op.split()[1])
    elif op.startswith('2'):
        deq.append(op.split()[1])
    elif op in ('3', '4', '7', '8'):
        if not deq:
            result.append('-1')
        elif op == '3':
         result.append(deq.popleft())
        elif op == '4':
            result.append(deq.pop())
        elif op == '7':
            result.append(deq[0])
        elif op == '8':
            result.append(deq[-1])
    elif op == '5':
        result.append(str(len(deq)))
    elif op == '6':
        if deq:
            result.append('0')
        else:
            result.append('1')
            
print('\n'.join(result))