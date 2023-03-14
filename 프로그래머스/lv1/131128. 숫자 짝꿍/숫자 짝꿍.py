def solution(X, Y):
    answer = ''
        
    xDict, yDict = {}, {}
    for i in X:
        if i in xDict:
            xDict[i] += 1
        else:
            xDict[i] = 1
        
    for i in Y:
        if i in yDict:
                yDict[i] += 1
        else:
            yDict[i] = 1
        
    interset = set(xDict.keys()) & set(yDict.keys())
        
    if len(interset) == 0:
        answer = '-1'
    else:
        interlist = sorted(list(interset))
        interlist.reverse()
        if interlist[0] == '0':
            answer = '0'
        else:
            for i in interlist:
                answer += i*xDict[i] if xDict[i] < yDict[i] else i*yDict[i]
    
    return answer