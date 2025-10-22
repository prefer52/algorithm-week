from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
for i in range(1, len(nums)):
    nums[i] = max(nums[i], nums[i-1] + nums[i])
    
print(max(nums))