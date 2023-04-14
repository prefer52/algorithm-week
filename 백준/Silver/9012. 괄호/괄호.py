from sys import stdin
from collections import deque

t, stack, result = int(stdin.readline()), deque(), deque()
case = [stdin.readline().rstrip() for i in range(t)]
for i in case:
    stack.clear()
    for j in i:
        if j == '(': stack.append(j)
        elif stack: stack.pop()
        else:
            result.append('NO')
            break
    else:
        if stack: result.append('NO')
        else: result.append('YES')
        
print('\n'.join(result))