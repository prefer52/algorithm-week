count = 0
move_info = []

def hanoi_tower(n, from_, by, to):
    global count, move_info
    count +=1
    if n == 1:
        move_info.append([from_, to])
    else:
        hanoi_tower(n-1, from_, to, by)
        move_info.append([from_, to])
        hanoi_tower(n-1, by, from_, to)
        

n = int(input())
hanoi_tower(n, 1, 2, 3)
print(count)
for i in range(count):
    print('%d %d' %(move_info[i][0], move_info[i][1]))