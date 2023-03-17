from sys import stdin

def Euclidean(a, b):
    r = a%b
    if r == 0:
        return b
    return Euclidean(b, r)

a1, b1 = tuple(map(int, stdin.readline().split()))
a2, b2 = tuple(map(int, stdin.readline().split()))

nomi = (b1*b2)//Euclidean(b1, b2)
deno = (a1 * (nomi//b1)) + (a2 * (nomi//b2))
gcd = Euclidean(nomi, deno)
print(deno//gcd, nomi//gcd)