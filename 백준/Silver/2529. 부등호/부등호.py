from sys import stdin
from itertools import permutations

k = int(stdin.readline())
signs = stdin.readline().split()
bigger = [(i,i+1) if sign=='<' else (i+1, i) for i, sign in enumerate(signs)]
sequences = list(permutations(range(10), k+1))
    
def result_seq(sequences):
    for seq in sequences:
        for pair in bigger:
            if seq[pair[0]] > seq[pair[1]]:
                break
        else:
            return ''.join(list(map(str, seq)))
    
print(result_seq(sequences[::-1]) + '\n' + result_seq(sequences))