from collections import Counter, deque

def solution(food_times, k):
    # 시간이 작은 순으로 정렬
    counter = deque(sorted((Counter(food_times).items())))
    # 남은 음식 수, 음식마다 소요된 공통 시간
    food_len, overtime = len(food_times), 0
    while counter and k - (counter[0][0]-overtime)*food_len >= 0:
        k -= (counter[0][0]-overtime)*food_len
        food_len -= counter[0][1]
        overtime = counter[0][0]
        counter.popleft()

    if not counter:
        return -1

    k %= food_len
    index = -1
    for i, time in enumerate(food_times):
        if time >= counter[0][0]:
            index += 1
            if index == k:
                return i+1