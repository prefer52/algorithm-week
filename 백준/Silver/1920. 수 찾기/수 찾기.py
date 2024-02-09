from sys import stdin

n = int(stdin.readline())
aList = sorted(list(map(int, stdin.readline().split())))
m = int(stdin.readline())
finds = list(map(int, stdin.readline().split()))
result = ''

for find in finds:
    start, end = 0, len(aList)-1
    while start <= end:
        mid = (start + end)//2
        if aList[mid] == find:
            result += '1'
            break
        elif aList[mid] > find:
            end = mid-1
        else:
            start = mid + 1
    if start > end:
        result += '0'

print('\n'.join(result))