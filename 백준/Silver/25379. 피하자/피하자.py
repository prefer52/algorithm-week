n = int(input())
seqs = list(map(int, input().split()))

counts, count = [], 0

even_seqs = seqs[:]
even_first = 0
even_count = 0 if even_seqs[0]%2 != 0 else 1 # 누적된 짝수 개수
for i in range(1, n): # 짝수를 앞으로
    if even_seqs[i]%2 == 0: # 만약 현재 수가 짝수이면
        count += i - even_count
        even_count += 1
even_first, count = count, 0

odd_count = 0  if seqs[0]%2 == 0 else 1 # 누적된 홀수 개수
for i in range(1, n):
    if seqs[i]%2 != 0: # 만약 현재 수가 홀수이면
        count += i - odd_count
        odd_count += 1
print(min(count, even_first))