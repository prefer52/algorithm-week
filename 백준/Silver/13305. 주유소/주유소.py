from sys import stdin

n = int(input())
dists = list(map(int, stdin.readline().split()))
costs = list(map(int, stdin.readline().split()))

total_cost = costs[0]*dists[0]
min_cost = costs[0]

for i in range(1, n-1):
    if costs[i] < min_cost:
        min_cost = costs[i]
    total_cost += dists[i]*min_cost
    
print(total_cost)