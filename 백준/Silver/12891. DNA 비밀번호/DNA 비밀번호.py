s, p = map(int, input().split())
dna = list(input().strip())
a, c, g, t = map(int, input().split())
alpha_count = {'A': 0, 'C':0, 'G':0, 'T':0}


for i in range(p):
    alpha_count[dna[i]] += 1

left, result = 0, 0
if alpha_count['A'] >= a and alpha_count['G'] >= g and alpha_count['C'] >= c and alpha_count['T'] >= t:
    result += 1
    
for r in range(p, len(dna)):
    alpha_count[dna[left]] -= 1
    alpha_count[dna[r]] += 1
    if alpha_count['A'] >= a and alpha_count['G'] >= g and alpha_count['C'] >= c and alpha_count['T'] >= t:
        result += 1
    left += 1

print(result)