def solution(cards):
    card_dict = dict(enumerate(cards,1))
    result = [0]
    for i in cards:
        if i in card_dict:
            box_num = 1
            card = card_dict.pop(i)
            while card in card_dict:
                card = card_dict.pop(card)
                box_num += 1
            result += [box_num]
            
    max_values = sorted(result, reverse=True)[0:2]
    return max_values[0]*max_values[1]