n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

max_budget = 0
if sum(budgets) < m:
    print(max(budgets))
else:
    start, end = 1, int(1e9)
    while start <= end:
        mid = (start + end)//2
        allocated_budgets = [budget if budget <= mid else mid for budget in budgets]
        if sum(allocated_budgets) > m:
            end = mid - 1
        else:
            max_budget = max(max_budget, max(allocated_budgets))
            start = mid + 1    
    print(max_budget)