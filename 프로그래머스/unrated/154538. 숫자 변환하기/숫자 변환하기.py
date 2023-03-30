def solution(x, y, n):
    count = [0 for i in range(y+1)]
    count[x] = 1
    if x == y: return 0
    while x < y:
        if count[x] > 0:
            case = [x+n, x*2, x*3]
            for j in case:
                if j <= y:
                    count[j] = count[x]+1 if count[j] == 0 else min(count[j], count[x]+1)
        x += 1
    return -1 if count[y] == 0 else count[y]-1

print(solution(10, 40, 5))