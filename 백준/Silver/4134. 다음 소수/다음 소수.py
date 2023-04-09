from sys import stdin

t = int(stdin.readline())
result, case = [], [int(stdin.readline()) for _ in range(t)]
for i in range(t):
    value = case[i]
    if value <= 2: result.append('2')
    else:
        while True:
            for j in range(2, int(value**0.5)+1):
                if value%j == 0: break
            else:
                result.append(str(value))
                break
            value += 1

print('\n'.join(result))