from collections import deque

n, k = map(int, input().split())

cost = [int(1e9)]*(200001)
deq = deque([n])
cost[n] = 0

while deq:
    pos = deq.popleft()
    moves = [1 , -1, pos]
    for move in moves:
        if 0 <= pos + move <= 200000 and cost[pos + move] == int(1e9):
            cost[pos + move] = cost[pos] + 1
            deq.append(pos+move)

print(cost[k])