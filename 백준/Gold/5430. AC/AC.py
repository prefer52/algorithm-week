from sys import stdin

t = int(input())
result = ""

for i in range(t):
    actions = stdin.readline().strip()
    n = int(stdin.readline())
    arr = list(stdin.readline().strip().lstrip('[').rstrip(']').split(','))
    if actions.count('D') > n:
        result += "error\n"
    else:
        pop = 0
        for action in actions:
            if action == 'R':
                pop = -1 if pop == 0 else 0
            elif action == 'D':
                arr.pop(pop)
        if pop == 0:
            result += '[' + ','.join(arr) + ']\n'
        else:
            result += '[' + ','.join(arr[::-1]) + ']\n'
        
print(result)