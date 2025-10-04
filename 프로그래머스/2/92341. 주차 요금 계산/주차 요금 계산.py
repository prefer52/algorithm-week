import math

def solution(fees, records):
    records = [record.split() for record in records]
    car_logs = {}
    for time, car, status in records:
        if car not in car_logs:
            car_logs[car] = []
        car_logs[car].append(time)
    
    time_logs = [times if len(times)%2 == 0 else times + ['23:59'] for car, times in sorted(car_logs.items(), key=lambda x: x[0])]
    result = []
    for times in time_logs:
        total_time = 0
        for i in range(0, len(times), 2):
            b_hour, b_minute = map(int, times[i].split(':'))
            a_hour, a_minute = map(int, times[i+1].split(':'))
            total_time += (a_hour*60 + a_minute) - (b_hour*60 + b_minute)
        result.append(fees[1] if total_time <= fees[0] else fees[1] + math.ceil((total_time - fees[0])/fees[2])*fees[3])
        
    return result