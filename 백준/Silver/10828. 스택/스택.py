from sys import stdin
from collections import deque

c = int(stdin.readline())
command, result = [stdin.readline() for i in range(c)], ''
stack = deque()
for i in command:
    if i.startswith('push'): stack.append(int(i.split()[1]))
    elif i.startswith('pop'):
        result += str(stack.pop()) + '\n' if stack else '-1\n'
    elif i.startswith('size'): result += str(len(stack)) + '\n'
    elif i.startswith('empty'):
        result += '1\n' if not stack else '0\n'
    else:
        result += str(stack[-1]) + '\n' if stack else '-1\n'
        
print(result)