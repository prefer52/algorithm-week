from sys import stdin

n, m = tuple(map(int, stdin.readline().split()))
book = {}
for i in range(n):
    book[stdin.readline().rstrip()] = str(i+1)
    
name_list = list(book.keys())

quiz = [''] * m
for i in range(m):
    quiz[i] = stdin.readline().rstrip()

result = [''] * m

for i in range(m):
    if quiz[i].isdigit():
        result[i] = name_list[int(quiz[i])-1]
    else:
        result[i] = book[quiz[i]]
        
print('\n'.join(result))