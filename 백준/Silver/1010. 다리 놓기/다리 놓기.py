from sys import stdin

t = int(stdin.readline())
factorial = [1] + [i for i in range(1, 31)]
for i in range(2, 31):
    factorial[i] *= factorial[i-1]
    
for _ in range(t):
    n, m = map(int, stdin.readline().split())
    print(factorial[m]//(factorial[m-n]*factorial[n]))