def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for wear in reserve[:]:
        if wear in lost:
            lost.pop(lost.index(wear))
            reserve.pop(reserve.index(wear))
    
    for wear in reserve:
        if wear - 1 in lost:
            lost.pop(lost.index(wear-1))
        elif wear + 1 in lost:
            lost.pop(lost.index(wear+1))

    return n - len(lost)