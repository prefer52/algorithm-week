from sys import stdin
from collections import deque

n, w, l = tuple(map(int, stdin.readline().split()))
weights = deque(list(map(int, stdin.readline().split())))
bridge = deque([0]*w)
move = 0

while weights:
    if l + bridge[0] >= weights[0]:
        bridge.append(weights.popleft())
        l += -bridge[-1] + bridge.popleft() 
        move += 1
    else:
        while bridge and l < weights[0]-bridge[0]:
            l += bridge.popleft()
            bridge.append(0)
            move += 1
            
print(move + w)