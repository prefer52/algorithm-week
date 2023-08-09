def solution(dirs):
    pos = [0, 0]
    move = {'U':(0,1), 'D':(0,-1), 'R':(1,0), 'L':(-1,0)}
    path_set = set()
    
    for dir in dirs:
        cur_pos = pos[:]
        for i in range(2):
            if abs(pos[i] + move[dir][i]) <= 5:
                pos[i] += move[dir][i]
        if cur_pos != pos:
            path_set.add(tuple(cur_pos + pos))
            path_set.add(tuple(pos + cur_pos))

    return len(path_set)//2