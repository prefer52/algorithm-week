from sys import stdin

n, k = map(int, stdin.readline().split())
kits = list(map(int, stdin.readline().split()))
count = 0

def backtracking(weight, day):
    if day == n or weight < 500:
        if weight >= 500:
            global count
            count += 1
        return
    
    for i in range(len(kits)):
        if kits[i] != 0:
            temp = kits[i]
            weight += kits[i] - k
            kits[i] = 0
            backtracking(weight, day+1)
            kits[i] = temp
            weight += -(kits[i] - k)

backtracking(500, 0)
print(count)