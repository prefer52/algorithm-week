from sys import stdin

k, n = map(int, stdin.readline().split())
lines = [int(stdin.readline()) for _ in range(k)]

# 가장 작은 랜선 길이와 현재 가진 랜선 중 가장 긴 랜선
# maxLength는 가장 긴 랜선의 길이를 저장하는 변수
start, end, maxLength = 1, max(lines), 0
while start <= end:
    mid = (start + end) // 2
    # 희망 랜선 길이로 잘라서 나온 개수의 총합 계싼
    # 만약 희망하는 개수 n개보다 많거나 같다면 랜선 길이를 늘리기
    if sum(line//mid for line in lines) >= n:
        maxLength, start = mid, mid + 1
    else:
        end = mid - 1
        
print(maxLength)