from sys import stdin

n = int(input())
timeInfos = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
timeInfos.sort(key=lambda x: (x[1], x[0]))

endTime, result = 0, 0

for timeInfo in timeInfos:
    if timeInfo[0] >= endTime:
        result += 1
        endTime = timeInfo[1]
        
print(result)