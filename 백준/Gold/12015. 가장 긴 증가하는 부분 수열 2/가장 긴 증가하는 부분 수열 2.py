from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

seqs = [nums[0]]
for i in range(1, n):
    if nums[i] > seqs[-1]:
        seqs.append(nums[i])
    else:
        start, end = 0, len(seqs) - 1
        while start <= end:
            mid = (start+end)//2
            if seqs[mid] < nums[i]:
                start = mid + 1
            else:
                end = mid - 1

        seqs[start] = nums[i]

print(len(seqs))