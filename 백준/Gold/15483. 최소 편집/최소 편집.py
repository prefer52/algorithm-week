org = ' ' + input()
dest = ' ' + input()
update = [[i for i in range(len(dest))]] + [[i] + [0]*(len(dest)-1) for i in range(1, len(org))]
for i in range(1, len(org)):
    for j in range(1, len(dest)):
        if org[i] == dest[j]:
            update[i][j] = update[i-1][j-1]
        else:
            update[i][j] = 1 + min(update[i][j-1], update[i-1][j], update[i-1][j-1])

print(update[len(org) - 1][len(dest) - 1])