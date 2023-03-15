from sys import stdin

def Euclidean(a, b):
    r = a % b
    if r == 0:
        return b
    return Euclidean(b, r)

a, b = tuple(map(int, stdin.readline().split()))
gcd = Euclidean(a, b)
lcm = abs(a*b)//gcd

print(lcm)