def solution(today, terms, privacies):
    result = []
    year, month, day = map(int, today.split('.'))
    day_sum = year*10000+(month-1)*100+day
    
    clause = {i.split()[0]:int(i.split()[1]) for i in terms}
    
    for i, info in enumerate(privacies):
        y, m, d = map(int, info.split()[0].split('.'))
        cla = str(info.split()[1])
        days = y*12*28 + (m-1)*28 + d + (clause[cla]-1)*28 + 28
        y, m = divmod(days, (12*28))
        m, d = divmod(m , 28)
        if day_sum >= y*10000+m*100+d:
            result.append(i+1)
            
    return result

print(solution('2022.05.19', ['A 6', 'B 12', 'C 3'], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))