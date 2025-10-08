from itertools import product

def solution(users, emoticons):
    results = []

    for case in product([10, 20, 30, 40], repeat=len(emoticons)):
        register, total_price = 0, 0
        for user in users:
            price = sum(int((100-case[i])*emoticons[i]*0.01) for i in range(len(case)) if case[i] >= user[0])
            if price >= user[1]:
                register += 1
            else:
                total_price += price
        results.append([register, total_price])
    
    return max(results, key=lambda x: (x[0], x[1]))