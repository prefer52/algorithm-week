from sys import stdin

def canhtore(lines, size):
    if size == 1:
        return lines
    
    size //= 3
    return canhtore(lines[:size], size) + [' ']*(size) + canhtore(lines[size*2:], size)

while True:
    n = stdin.readline()
    if not n:
        break
    n = int(n)
    lines = ['-']*(3**n)
    print(''.join(canhtore(lines, 3**n)))