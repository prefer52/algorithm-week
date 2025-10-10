from sys import stdin

t = int(stdin.readline())
min_length, max_length = 10001, 0
for _ in range(t):
    chr_count = {chr(ord('a')+i):[] for i in range(26)}
    string = stdin.readline().strip()
    k = int(stdin.readline())
    for i in range(len(string)):
        chr_count[string[i]].append(i)
    
    min_length, max_length = 10001, 0
    for alpha in chr_count.keys():
        if len(chr_count[alpha]) >= k:
            for i in range(len(chr_count[alpha]) - (k-1)):
                length = chr_count[alpha][i+k-1] - chr_count[alpha][i] + 1
                min_length, max_length = min(min_length, length), max(max_length, length)
                
    
    if max_length > 0:
        print(min_length, max_length)
    else:
        print(-1)