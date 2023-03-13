from sys import stdin

n = int(stdin.readline())
NCard = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
MCard = list(map(int, stdin.readline().split()))

NCard.sort()
NCount = []
i = 0
while (i < n):
    j = i+1
    while (j < n) and (NCard[j] == NCard[j-1]):
        j += 1
    NCount.append((NCard[j-1], j - i))
    i = j
result = []

for i in MCard:
    ch_flag = 0
    min, max =0, len(NCount)-1
    while(min <= max):
        mid = (min + max)//2
        if NCount[mid][0] == i:
            result.append(str(NCount[mid][1]))
            ch_flag = 1
            break
        else:
            if NCount[mid][0] > i:
                max = mid-1
            else:
                min = mid+1
    if ch_flag == 0:
        result.append('0')
        
print(' '.join(result))