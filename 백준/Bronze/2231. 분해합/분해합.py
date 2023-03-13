n = int(input())

consturctor = []
for i in range(n+1):
    c = i
    sum = c
    while(c // 10 != 0):
        sum += c % 10
        c //= 10
    sum += c % 10
    if sum == n:
        consturctor.append(i)
        break
        
if len(consturctor) != 0:
    print(consturctor[0])
else:
    print(0)