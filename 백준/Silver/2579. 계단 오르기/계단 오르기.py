from sys import stdin

n = int(stdin.readline())
stairs = [0] + [int(stdin.readline()) for _ in range(n)]
scores = [[-1, -1] for _ in range(n+1)]

def score(pos, seq):
    if pos < 0:
        return 0
    
    if scores[pos][seq] == -1:
        if seq == 0:
            scores[pos][seq] = stairs[pos] + score(pos-2, 1)
        else:
            scores[pos][seq] = stairs[pos] + max(score(pos-1, 0), score(pos-2, 1))
    return scores[pos][seq]

print(score(n, 1))