import itertools
from collections import deque

def solution(expression):
    op = ['+', '-', '*']
    num_only, op_only = expression[:], ''
    
    for i in op:
        num_only = num_only.replace(i, ' ')
    num_only = num_only.split()
    for i in expression:
        if i in op:
            op_only += i

    result_list, prior_list = [], list(itertools.permutations(op, 3))
    for case in prior_list:
        num_list, op_list = num_only[:], op_only[:]
        for i in case:
            while op_list.find(i) != -1:
                index = op_list.find(i)
                num_list[index] = eval(str(num_list[index]) + i + str(num_list[index+1]))
                del num_list[index+1]
                op_list = op_list.replace(i, '', 1)
        result_list.append(abs(int(num_list[0])))
    return max(result_list)