from collections import deque

n = int(input())
deq = deque(range(1, n+1))

if n == 1:
    print(1)
else:
    while True:
        deq.popleft()
        if len(deq) == 1:
            break
        deq.append(deq.popleft())

    print(deq.pop())