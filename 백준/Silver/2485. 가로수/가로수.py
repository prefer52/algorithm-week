from sys import stdin

def Euclidean(a, b):
    r = a%b
    if r == 0:
        return b
    return Euclidean(b, r)

n = int(stdin.readline())
space = [0]*(n-1)

pos_1 = int(stdin.readline())
for i in range(n-1):
    pos_2 = int(stdin.readline())
    space[i] = pos_2 - pos_1
    pos_1 = pos_2

result = Euclidean(space[0], space[1])
for i in range(2, n-1):
    lsm = Euclidean(result, space[i])
    result = lsm if lsm < result else result

least_num = 0
for i in range(n-1):
    least_num += space[i]//result - 1
    
print(least_num)