from sys import stdin
n = int(stdin.readline())
sequence = list(map(int, stdin.readline().split()))
mem = [1]*n

for i in range(1, n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            mem[i] = max(mem[i], mem[j] + 1)
            
print(max(mem))