def solution(n, t, m, p):
    game_str, pos_dict = '0', {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    
    for num in range(1, m*(t - 1) + p + 1):
        pos_num = ''
        while num > 0:
            num, mod = divmod(num, n)
            pos_num += pos_dict[mod]
        game_str += pos_num[::-1]
    
    return ''.join([game_str[turn*m + p-1] for turn in range(t)])