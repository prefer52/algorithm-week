n = int(input())
cards = list(map(int, input().split()))

# 각 카드마다 오른쪽(direction=1, 왼쪽은 -1) 카드 간격을 기준으로 간격 균일화했을 때 변경해야 하는 전체 수 계산
def count_min_change(direction):
    min_change = 1e9
    ranges = range(n-1) if direction == 1 else range(n-1, 0, -1)
    for i in ranges:
        result = 0
        diff = direction * cards[i+direction] - direction * cards[i]
        for j in range(i+1, n):
            if cards[j] != cards[i] + diff*(j-i):
                result += 1
        for j in range(i-1, -1, -1):
            if cards[j] != cards[i] - diff*(i-j):
                result += 1
        min_change = min(result, min_change)
    return min_change
    
print(min(count_min_change(1), count_min_change(-1)))