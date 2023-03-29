def solution(today, terms, privacies):
    result = []
    year, month, day = map(int, today.split('.'))
    day_sum = year*10000+(month-1)*100+day
    clause = {i.split()[0]:int(i.split()[1]) for i in terms}
    
    for i, info in enumerate(privacies):
        date, cla = info.split()
        y, m, d = map(int, date.split('.'))
        days = y*12*28 + (m-1)*28 + d + clause[cla]*28
        y, m = divmod(days, (12*28))
        m, d = divmod(m , 28)
        if day_sum >= y*10000+m*100+d: result.append(i+1)
        
    return result