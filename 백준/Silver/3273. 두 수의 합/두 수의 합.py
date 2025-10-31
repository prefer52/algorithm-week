n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
start, end = 0, n-1

result = 0
while start < n-1 and start < end:
    num_sum = nums[start] + nums[end]
    if num_sum == x:
        result += 1
        start += 1
    elif num_sum < x:
        start += 1
    elif num_sum > x:
        end -=1

print(result)