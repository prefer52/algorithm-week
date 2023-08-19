def solution(targets):
    targets.sort()
    answer, min_e = 0, targets[0][1]
    for target in targets:
        if target[0] < min_e:
            min_e = min(target[1], min_e)
        else:
            min_e = target[1]
            answer += 1
            
    return answer+1