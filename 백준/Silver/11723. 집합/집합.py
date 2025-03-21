from sys import stdin

m = int(stdin.readline())
result, s = '', 0

for i in range(m):
    op = stdin.readline().strip().split()
    
    if op[0] == 'add':
        s |= 1 << int(op[1])
    elif op[0] == 'remove':
        s &= ~(1 << int(op[1]))
    elif op[0] == 'check':
        if s & 1 << int(op[1]):
            print('1')
        else:
            print('0')
    elif op[0] == 'toggle':
        s ^= 1 << int(op[1])
    else:
        s = 0b111111111111111111110 if op[0] == 'all' else 0