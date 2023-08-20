def solution(cards):
    card_dict = dict(enumerate(cards,1))
    result = []
    for i in cards:
        if i in card_dict:
            box_num = 1
            card = card_dict.pop(i)
            while card in card_dict:
                card = card_dict.pop(card)
                box_num += 1
            result += [box_num]
    max_value1 = max(result)
    result.remove(max_value1)
    if result:
        max_value2 = max(result)
        result.remove(max_value2)
        return max_value1*max_value2
    else:
        return 0