def solution(ingredient):
    hamburger = ''.join(list(map(str, ingredient)))
    burger = ['0', '0', '0']
    for i in hamburger:
        burger.append(i)
        if burger[-4:] == ['1', '2', '3', '1']: del(burger[-4:])
    return (len(ingredient) - (len(burger)-3))//4
