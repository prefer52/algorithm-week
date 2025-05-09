n, k = map(int, input().split())
seqs = list(map(int, input().split()))

left, right = 0, k
max_sum = sum(seqs[left:right])
cur_sum = max_sum

for r in range(right, len(seqs)):
    temper_sum = cur_sum + seqs[r] - seqs[left]
    max_sum = max(temper_sum, max_sum)
    cur_sum = temper_sum
    left += 1
    
print(max_sum)