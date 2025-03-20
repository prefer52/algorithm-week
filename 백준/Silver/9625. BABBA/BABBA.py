k = int(input())

count = [[1, 0]] + [[0, 0] for _ in range(k)]

for i in range(1, k+1):
    count[i][0] = count[i-1][1]
    count[i][1] = count[i-1][0] + count[i-1][1]
    
print(' '.join(map(str, count[k])))