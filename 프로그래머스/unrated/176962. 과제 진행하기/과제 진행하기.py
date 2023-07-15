from collections import deque

def solution(plans):
    result, stack = [], deque()
    length = len(plans)
    for plan in plans:
        time = list(map(int, plan[1].split(':')))
        plan[1] = time[0]*60 + time[1]
        plan[2] = int(plan[2])
        
    plans.sort(key=lambda x:x[1])
    time = plans[0][1]
    for i in range(length-1):
        if time + plans[i][2] > plans[i+1][1]:
            plans[i][2] -= (plans[i+1][1] - plans[i][1])
            stack.append(plans[i])
            time = int(plans[i+1][1])
        else:
            result.append(plans[i][0])
            time = plans[i][1] + plans[i][2]
            if plans[i+1][1] != time and stack:
                stopped_plan = stack.pop()
                time += stopped_plan[2]
                while time <= plans[i+1][1]:
                    result.append(stopped_plan[0])
                    if stack:
                        stopped_plan = stack.pop()
                        time += stopped_plan[2]
                    else:
                        break
                if time > plans[i+1][1]:
                    stopped_plan[2] = time - plans[i+1][1]
                    stack.append(stopped_plan)
                time = plans[i+1][1]
            else:
                time = plans[i+1][1]
    result.append(plans[-1][0])
    while stack:
        result.append(stack.pop()[0])
        
    return result