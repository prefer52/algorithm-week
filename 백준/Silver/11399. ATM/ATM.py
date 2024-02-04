n = int(input())
times = sorted(list(map(int, input().split())))
for i in range(1, len(times)):
    times[i] += times[i-1]

print(sum(times))