n, m = map(int, input().split())

result = []
def backtracking(select_count, seq, start):
    if select_count == m:
        result.append(seq)
        
    for i in range(start, n+1):
        seq.append(i)
        backtracking(select_count + 1, seq[:], i+1)
        seq.pop()

result.sort()
backtracking(0, [], 1)
print('\n'.join([' '.join(map(str, seq)) for seq in result]))