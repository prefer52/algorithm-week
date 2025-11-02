n, m = map(int, input().split())

def backtracking(seqs, n, m, result):
    if len(seqs) == m:
        result.append(' '.join(map(str, seqs)))
        return

    for i in range(seqs[-1], n+1):
        seqs.append(i)
        backtracking(seqs, n, m, result)
        seqs.pop()

result = []
for i in range(1, n+1):
    backtracking([i], n, m, result)
print('\n'.join(sorted(result)))