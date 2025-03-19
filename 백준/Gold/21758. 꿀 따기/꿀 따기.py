from sys import stdin

n = int(stdin.readline())
honeys = list(map(int, stdin.readline().split()))

left_honeys = honeys[:]
for i in range(2, len(honeys)):
    left_honeys[i] = left_honeys[i] + left_honeys[i-1]
left_honey = max([left_honeys[-1] - honeys[i] + (left_honeys[-1] - left_honeys[i])for i in range(1, len(honeys))])

right_honeys = honeys[:]
for i in range(len(honeys) - 3, -1, -1):
    right_honeys[i] = right_honeys[i] + right_honeys[i+1]
right_honey = max([right_honeys[0] - honeys[i] + (right_honeys[0] - right_honeys[i])for i in range(len(honeys) - 2, -1, -1)])

mid_honeys = [left_honeys[i] + right_honeys[i] for i in range(len(honeys))]
mid_honeys[0], mid_honeys[-1] = 0, 0
mid_honey = max(mid_honeys)

print(max(left_honey, mid_honey, right_honey))