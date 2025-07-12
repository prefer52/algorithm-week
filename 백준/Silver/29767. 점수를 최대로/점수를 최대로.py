from sys import stdin

n, k = map(int, stdin.readline().split())
scores = list(map(int, stdin.readline().split()))
for i in range(1, n):
    scores[i] += scores[i-1]
    
scores.sort(reverse=True)
print(sum(scores[:k]))