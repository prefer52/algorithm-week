from sys import stdin

def find_parent(parents, x):
    x_parent = x
    while parents[x_parent] != x_parent:
        x_parent = parents[x_parent]
    parents[x] = x_parent
    return parents[x]

def union(a, b, parents):
    a = find_parent(parents, a)
    b = find_parent(parents, b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
        
n, m = map(int, stdin.readline().split())
parents = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = list(map(int, stdin.readline().split()))
    if op:
        print('YES') if find_parent(parents, a) == find_parent(parents, b) else print('NO')
    else:
        union(a, b, parents)