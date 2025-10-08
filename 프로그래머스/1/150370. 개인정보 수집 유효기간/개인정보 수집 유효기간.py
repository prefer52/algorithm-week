def solution(today, terms, privacies):
    result, deadline = [], get_days(today)
    term_dict = {term[0]:int(term[2:])*28 for term in terms}
    
    return [no for no, privacy in enumerate(privacies, start=1) if get_days(privacy[:10]) + term_dict[privacy[11]] <= deadline]


def get_days(date):
    year, month, day = date.split(".")
    return int(year)*12*28 + int(month)*28 + int(day)