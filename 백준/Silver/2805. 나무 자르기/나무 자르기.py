from sys import stdin

n, m = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

start, end, maxHeight = 1, max(trees), 0
while start <= end:
    mid = (start + end) // 2
    treeSum = sum(tree - mid for tree in trees if tree - mid > 0)
    if treeSum >= m:
        maxHeight, start = mid, mid + 1
    else:
        end = mid - 1
        
print(maxHeight)