n, k = map(int, input().split())

result = []
people = [str(i + 1) for i in range(n)]

index = 0
while people:
    index = (index + k - 1) % len(people)
    result += [people.pop(index)]

print('<' + ', '.join(result) + '>')