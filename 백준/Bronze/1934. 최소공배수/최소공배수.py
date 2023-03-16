from sys import stdin

def Euclidean(a, b):
    r = a % b
    if r == 0:
        return b
    return Euclidean(b, r)
    
t = int(stdin.readline())
lsm = [''] * t
for i in range(t):
    a, b = tuple(map(int, stdin.readline().split()))
    lsm[i] = str((a*b) // Euclidean(a, b))
    
print('\n'.join(lsm))