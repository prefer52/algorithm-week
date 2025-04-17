from sys import stdin

n = int(stdin.readline())
numbers = [0] + [int(stdin.readline()) for _ in range(n)]
adjs = [[] for _ in range(n+1)]

for idx, number in enumerate(numbers):
    adjs[number].append(idx)

results = []
for i in range(1, n+1):
    stack = [i]
    visited = [False] * (n+1)
    visited[i] = True
    while stack:
        number = stack.pop()
        for adj_number in adjs[number]:
            if adj_number == i:
                results.append(i)
                break
            else:
                if not visited[adj_number]:
                    visited[adj_number] = True
                    stack.append(adj_number)
        else:
            continue
        break

print(len(results), '\n'.join(list(map(str, sorted(results)))), sep='\n')