import math

def solution(fees, records):
    answer = []
    car_dict = dict()
    for record in records:
        record = record.split()
        time = list(map(int, record[0].split(':')))
        record[0] = time[0]*60 + time[1]
        if car_dict.get(record[1]):
            car_dict[record[1]].append(record[0])
        else:
            car_dict[record[1]] = [record[0]]
            
    time_list = sorted(car_dict.items(), key=lambda x:x[0])
    park_time = []
    for time in list(zip(*time_list))[1]:
        if len(time) % 2 != 0:
            time.append((23*60 + 59))
        park_time.append([time[i+1]-time[i] for i in range(0, len(time), 2)])
    
    park_time = [sum(times) for times in park_time]
    for fee in park_time:
        if fee <= fees[0]:
            fee = fees[1]
        else:
            fee = fees[1] + (math.ceil((fee-fees[0])/fees[2]))*fees[3]
        answer.append(fee)
    
    return answer