def solution(id_list, report, k):
    report_set = set(report)
    dict_report = {}
    for i in report_set:
        userID, reportID = tuple(i.split())
        if reportID in dict_report: dict_report[reportID].append(userID)
        else: dict_report[reportID] = [userID]
    
    result = [0]*len(id_list)
    for i in list(dict_report.values()):
            for j in i: result[id_list.index(j)] += 1 if len(i) >= k else 0
    return result
