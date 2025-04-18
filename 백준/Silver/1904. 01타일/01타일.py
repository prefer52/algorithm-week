n = int(input())
if n <= 2:
    print(n)
else:
    prev, two_prev = 2, 1
    for i in range(3, n+1):
        curr = (prev + two_prev) % 15746
        prev, two_prev = curr, prev
    print(curr)