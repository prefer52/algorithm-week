from sys import stdin

n = int(stdin.readline())
numbers = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
find_numbers = list(map(int, stdin.readline().split()))

result = []
for find_number in find_numbers:
    start, end, mid = 0, len(numbers) - 1, 0
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == find_number:
            result.append('1')
            break
        elif numbers[mid] > find_number:
            end = mid - 1
        else:
            start = mid + 1
    else:
        result.append('0')
        
print('\n'.join(result))