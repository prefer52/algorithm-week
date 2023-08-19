def solution(targets):
    targets.sort()
    answer, min_missile = 0, targets[0]
    for target in targets:
        if min_missile[0] <= target[0] < min_missile[1]:
            min_missile = [target[0], min(target[1], min_missile[1])]
        else:
            min_missile = target
            answer += 1
                        
    return answer+1