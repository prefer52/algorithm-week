from itertools import product

def solution(users, emoticons):
    pl = [[int(emoticons[i]*(100 - j*10)/100) for j in range(1, 5)] for i in range(len(emoticons))]
    seq = list(product(range(3, -1, -1), repeat=len(emoticons)))
    value_list = [[0, 0, 0, 0] for i in range(len(seq))]
    for i in range(len(seq)):
        for j in range(len(emoticons)): value_list[i][seq[i][j]] += pl[j][seq[i][j]]
        for j in range(2, -1, -1): value_list[i][j] += value_list[i][j+1]
    
    result = [[0, 0] for i in range(len(seq))]
    for i in range(len(seq)):
        for j in users:
            if value_list[i][(j[0]-1)//10] >= j[1]: result[i][0]+=1
            else: result[i][1] += value_list[i][(j[0]-1)//10]
    return max(i for i in result)