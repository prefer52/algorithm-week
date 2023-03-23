def solution(babbling):
    result = 0
    for i in babbling:
        if '*' in i.replace('ayaaya', '*').replace('woowoo', '*').replace('mama', '*').replace('yeye', '*'): continue
        if i.replace('aya', ' ').replace('woo', ' ').replace('ma', ' ').replace('ye', ' ').replace(' ', '') == '': result += 1
    return result