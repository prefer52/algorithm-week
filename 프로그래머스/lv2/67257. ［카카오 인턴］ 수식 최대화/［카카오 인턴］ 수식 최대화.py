import itertools
from collections import deque

def solution(expression):
    op = ['+', '-', '*']
    num_only, op_only = expression[:], ''
    
    for i in op:
        num_only = num_only.replace(i, ' ')
    num_only = list(map(int, num_only.split()))
    for i in expression:
        if i in op:
            op_only += i

    max, prior_list = 0, list(itertools.permutations(op, 3))
    for case in prior_list:
        num_list, op_list = num_only[:], op_only[:]
        for i in case:
            while op_list.find(i) != -1:
                index = op_list.find(i)
                if i == '+':
                    num_list[index] += num_list[index+1]
                elif i == '-':
                    num_list[index] -= num_list[index+1]
                else:
                    num_list[index] *= num_list[index+1]
                del num_list[index+1]
                op_list = op_list.replace(i, '', 1)
        if abs(num_list[0]) > max:
            max = abs(num_list[0])
    return max