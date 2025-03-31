from sys import stdin

n, k = map(int, stdin.readline().split())
poses = list(stdin.readline().strip())
count = 0

for i in range(len(poses)):
    if poses[i] == 'P':
        left_range = i - k if i - k >= 0 else 0
        right_range = i + k if i + k < len(poses) else len(poses) - 1
        for j in range(left_range, right_range+1):
            if poses[j] == 'H':
                poses[j] = 'E'
                break

print(poses.count('E'))