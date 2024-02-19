import copy

def canSolve(lx, ly, key, lock):
    for x in range(len(key)):
        for y in range(len(key)):
            lock[lx+x][ly+y] += key[x][y]
    for row in lock:
        if (0 in row) or (2 in row):
            return False
    return True

def solution(key, lock):
    keys = [key]
    keys.append([row[::-1] for row in zip(*key)])
    keys.append([row[::-1] for row in key[::-1]])
    keys.append([row for row in list(zip(*key))[::-1]])
    lock = [[-99] * (len(key)-1) + row + [-99] * (len(key)-1) for row in lock]
    lock = [[-99]*len(lock[0])]*(len(key)-1) + lock + [[-99]*len(lock[0])]*(len(key)-1)
    
    for row in lock:
        if 0 in row:
            break
    else:
        return True
    
    for key in keys:
        for lx in range(len(lock)-(len(key) - 1)):
            for ly in range(len(lock)-(len(key) - 1)):
                if canSolve(lx, ly, key, copy.deepcopy(lock)):
                    return True
    return False