n = int(input())
seqs = list(map(int, input().split()))

counts, count = [], 0

even_seqs = seqs[:]
even_first, switched = 0, False
for i in range(1, n): # 짝수를 앞으로
    if even_seqs[i]%2 == 0:
        for j in range(i-1, -1, -1):
            if even_seqs[j]%2 == 0:
                break
            even_seqs[j], even_seqs[i] = even_seqs[i], even_seqs[j]
            count += 1
even_first, count = count, 0
    
for i in range(1, n):
    if seqs[i]%2 != 0: # 홀수를 앞으로
        for j in range(i-1, -1, -1):
            if seqs[j]%2 != 0:
                break
            seqs[j], seqs[i] = seqs[i], seqs[j]
            count += 1
print(min(count, even_first))