import math

def solution(str1, str2):
    str1_dict, str2_dict = dict(), dict()
    str1_set, str2_set = set(), set()
    for i in range(len(str1)-1):
        string = str1[i:i+2].upper()
        if not string.isalpha():
            continue
        if string not in str1_dict:
            str1_dict[string] = 0
        str1_dict[string] += 1
        str1_set.add(string+str(str1_dict[string]))
    
    for i in range(len(str2)-1):
        string = str2[i:i+2].upper()
        if not string.isalpha():
            continue
        if string not in str2_dict:
            str2_dict[string] = 0
        str2_dict[string] += 1
        str2_set.add(string+str(str2_dict[string]))
        
    return math.floor((len(str1_set & str2_set)/len(str1_set | str2_set))*65536) if len(str1_set | str2_set) != 0 else 65536