from collections import deque

string = input()
a_count = string.count('a')
string += string[:a_count-1]

window = deque(list(string[:a_count]))
min_change = window.count('b')
change = min_change
if 'a' not in string:
    print(0)
else:
    for i in range(a_count, len(string)):
        change += ord('a') - ord(window.popleft()) + ord(string[i]) - ord('a')
        window.append(string[i])
        min_change = min(change, min_change)
        
    print(min_change)