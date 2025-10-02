def solution(N, stages):
    players, failures = len(stages), [[i,0] for i in range(N+1)]
    stages.sort()
    stages.reverse()

    for i in range(1, N+1):
        if not stages:
            break
            
        if stages[-1] <= i:
            while stages and stages[-1] <= i:
                stages.pop()
        failures[i][1] = (players - len(stages))/players
        players = len(stages)
        
    return list(zip(*sorted(failures[1:], key=lambda player: (-player[1], player[0]))))[0]