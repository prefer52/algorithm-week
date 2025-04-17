n, s = map(int, input().split())
numbers = list(map(int, input().split()))

min_length = 100001
start, number_sum = 0, 0
for end in range(n):
    number_sum += numbers[end]
    if number_sum >= s:
        while start <= end and number_sum - numbers[start] >= s:
            number_sum -= numbers[start]
            start += 1
        min_length = min(min_length, end - start + 1)

if min_length == 0:
    print(1)
elif min_length != 100001:
    print(min_length)
else:
    print(0)