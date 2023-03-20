from sys import stdin

def eratos(isPrimeNumber):
    isPrimeNumber[0] = isPrimeNumber[1] = False
    for i in range(2, 1001):
        j = i*2
        while j < 1000001:
            isPrimeNumber[j] = False
            j += i
            
isPrimeNumber = [True]*1000001
eratos(isPrimeNumber)
t = int(stdin.readline())
result = ['']*t
prime_list = [i for i in range(2, 1000001) if isPrimeNumber[i]]

for i in range(t):
    case = int(stdin.readline())
    num = 0
    for j in prime_list:
        if j > (case//2):
            break
        if isPrimeNumber[case-j]:
            num +=1
    
    result[i] = str(num)
        
print('\n'.join(result))