def dfs(numbers, result, index, add, sub, mul, div, results):
    if index == len(numbers):
        results.append(result)
    else:
        if add:
            dfs(numbers, result + numbers[index], index+1, add-1, sub, mul, div, results)
        if sub:
            dfs(numbers, result - numbers[index], index+1, add, sub-1, mul, div, results)
        if mul:
            dfs(numbers, result * numbers[index], index+1, add, sub, mul-1, div, results)
        if div:
            result = -((-result)//numbers[index]) if result < 0 else result//numbers[index]
            dfs(numbers, result, index+1, add, sub, mul, div-1, results)


n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
results = []
dfs(numbers, numbers[0], 1, add, sub, mul, div, results)
print(str(max(results)) + '\n' + str(min(results)))