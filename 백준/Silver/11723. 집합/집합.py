from sys import stdin

m = int(input())
S, result = 0, ''
init = (1<<21) - 1

for i in range(m):
    op = stdin.readline().split()
    if len(op) == 2:
        if op[0] == "add":
            S |= 1 << int(op[1])
        elif op[0] == "remove":
            S &= ~(1 << int(op[1]))
        elif op[0] == "check":
            print(str(int((S & (1 << int(op[1]))) > 0)))
        elif op[0] == "toggle":
            S ^= 1 << int(op[1])
    else:
        S = init if op[0] == 'all' else 0