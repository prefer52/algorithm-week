n, m = tuple(map(int, input().split()))

result = 0

S = set()
for i in range(n):
    S.add(input())

for i in range(m):
    v = input()
    if v in S:
        result += 1
        
print(result)