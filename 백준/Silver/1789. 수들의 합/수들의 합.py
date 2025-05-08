s = int(input())
count = 0
for i in range(1, s + 2):
    if s - i >= 0:
        s -= i
        count += 1
    else:
        print(count)
        break