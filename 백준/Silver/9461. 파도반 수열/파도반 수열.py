from sys import stdin

t = int(stdin.readline())
cases = [int(stdin.readline()) for _ in range(t)]

pados = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0]*90
for i in range(10, 100):
    pados[i] = pados[i-1] + pados[i-5]

print('\n'.join([str(pados[case-1]) for case in cases]))