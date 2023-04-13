from sys import stdin
from collections import deque

k, stack  = int(stdin.readline()), deque()
for i in range(k):
    num = int(stdin.readline())
    if num == 0: stack.pop()
    else: stack.append(num)
    
print(sum(stack))