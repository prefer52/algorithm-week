def solution(n, times):
    low, high = 1, 100000000000000
    time = 0
    while low <= high:
        mid = (low + high)//2
        count = sum(list(map(lambda x: mid//x, times)))
        if count < n:
            low = mid + 1
        else:
            time = mid
            high = mid - 1
    return time
            