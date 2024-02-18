from collections import Counter, deque

def solution(food_times, k):
    times = deque(sorted((Counter(food_times).items())))
    food_len, overtime = len(food_times), 0
    for time, foods_count in list(times):
        remain_time = k - (time - overtime)*food_len
        if not times:
            return -1
        if remain_time < 0:
            break
        k, overtime = remain_time, time
        food_len -= foods_count
        times.popleft()

    if not times:
        return -1
    
    k %= food_len
    return [i+1 for i in range(len(food_times)) if food_times[i] >= times[0][0]][k]