from sys import stdin
from collections import deque

string, stack = [], deque()
while True:
    line = stdin.readline()
    if line == '.\n':break
    string.append(line)
result = []

for i in string:
    stack.clear()
    for j in i:
        if j == '(' or j == '[': stack.append(j)
        elif j == ')':
            if not stack or stack[-1] != '(':
                result.append('no')
                break
            else: stack.pop()
        elif j == ']':
            if not stack or stack[-1] != '[':
                result.append('no') 
                break
            else: stack.pop()
    else:
        if stack: result.append('no')
        else: result.append('yes')

print('\n'.join(result))