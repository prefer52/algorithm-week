def solution(id_list, report, k):
    dict_report = {}
    for i in set(report):
        userID, reportID = tuple(i.split())
        dict_report[reportID] = dict_report[reportID] + [userID] if reportID in dict_report else [userID]
    
    result = [0]*len(id_list)
    for i in list(dict_report.values()):
            for j in i: result[id_list.index(j)] += 1 if len(i) >= k else 0
    return result