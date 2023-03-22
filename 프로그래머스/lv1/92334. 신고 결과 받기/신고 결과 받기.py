def solution(id_list, report, k):
    report_set = set(report)
    dict_report = {}
    for i in report_set:
        userID, reportID = tuple(i.split())
        if reportID in dict_report: dict_report[reportID].append(userID)
        else: dict_report[reportID] = [userID]
    
    result = [0]*len(id_list)
    for i in id_list:
        if dict_report.get(i) and len(dict_report[i]) >= k:
            for j in dict_report[i]: result[id_list.index(j)] += 1
    return result