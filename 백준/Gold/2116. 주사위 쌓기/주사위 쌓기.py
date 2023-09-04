from sys import stdin

pair = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

n = int(stdin.readline())
dices = [list(map(int, stdin.readline().split())) for _ in range(n)]
results, six_side = [], range(1,7)

for upper_side in six_side:
    result = 0
    for dice in dices:
        index = dice.index(upper_side)
        result += max(set(six_side) - set([dice[index], dice[pair[index]]]))
        upper_side = dice[pair[index]]
    results.append(result)
    
print(max(results))