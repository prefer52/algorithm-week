n, m = map(int, input().split())
mems = list(map(int, input().split()))
costs = list(map(int, input().split()))
total_cost = sum(costs)

apps = [[0]*(total_cost+1) for _ in range(n)]
for app in range(n):
    for cost in range(total_cost + 1):
        not_off_mem = apps[app-1][cost]
        off_mem = apps[app-1][cost-costs[app]] + mems[app] if cost-costs[app] >= 0 else 0
        apps[app][cost] = max(not_off_mem, off_mem)

for cost in range(total_cost+1):
    if apps[n-1][cost] >= m:
        print(cost)
        break