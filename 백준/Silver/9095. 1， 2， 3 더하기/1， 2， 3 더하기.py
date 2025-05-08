from sys import stdin

t = int(stdin.readline())
numbers = [int(stdin.readline()) for _ in range(t)]
mem = [0]*12
mem[1], mem[2], mem[3] = 1, 2, 4
for i in range(4, len(mem)):
    mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
        
for n in numbers:
    print(mem[n])