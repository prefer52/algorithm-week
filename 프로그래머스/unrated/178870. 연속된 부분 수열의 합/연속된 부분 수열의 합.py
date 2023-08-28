from collections import deque

def solution(sequence, k):
    result = []
    queue = deque()
    for i in enumerate(sequence):
        k -= i[1]
        queue.append(i)
        while k < 0:
            k += queue.popleft()[1]

        if k == 0:
            result += [[len(queue), queue[0][0], queue[-1][0]]]
            
    result.sort(key=lambda x:(x[0], x[1]))
    
    return [result[0][1], result[0][-1]]