from sys import stdin

n = int(stdin.readline())
liquids = list(map(int, stdin.readline().split()))

start, end = 0, n-1
min_sum = abs(liquids[start] + liquids[end])
min_start, min_end = 0, n-1

while start < end:
    liquid_sum = liquids[start] + liquids[end]
    if min_sum > abs(liquid_sum):
        min_sum = abs(liquid_sum)
        min_start, min_end = start, end

    if liquid_sum > 0:
        end -= 1
    else:
        start += 1

print(liquids[min_start], liquids[min_end])