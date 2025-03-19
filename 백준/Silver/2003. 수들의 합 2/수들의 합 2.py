from sys import stdin

n, m = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))
start, end, number_sum = 0, 0, numbers[0]
number_len = len(numbers)
count = 0

while True:
    if number_sum == m:
        count, end = count + 1, end + 1
        if end >= number_len:
            break
        number_sum += numbers[end]
    elif number_sum < m:
        end += 1
        if end >= number_len:
            break
        number_sum += numbers[end]
    else:
        number_sum, start = number_sum - numbers[start], start + 1
        if start >= number_len:
            break
    
print(count)