from sys import stdin

n, m = map(int, stdin.readline().split())
numbers = [0] + list(map(int, stdin.readline().split()))
ranges = [list(map(int, stdin.readline().split())) for i in range(m)]

for i in range(1, len(numbers)):
    numbers[i] = numbers[i-1] + numbers[i]

print('\n'.join([str(numbers[end] - numbers[start-1]) for start, end in ranges]))