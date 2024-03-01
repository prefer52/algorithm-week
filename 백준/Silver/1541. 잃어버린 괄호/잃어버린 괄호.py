exprs = input().split('-')
numbers = []

def getNumber(number):
    if number == '0':
        return 0
    elif number.startswith('0'):
        for idx in range(5):
            if number[idx] != '0':
                break
        return int(number[idx:])
    else:
        return int(number)

for expr in exprs:
    result = 0
    if '+' in expr:
        expr = expr.split('+')
        for number in expr:
            result += getNumber(number)
    else:
        result += getNumber(expr)
    numbers.append(result)

print(numbers[0] - sum(numbers[1:]))