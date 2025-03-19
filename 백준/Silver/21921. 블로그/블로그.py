from sys import stdin

n, x = map(int, stdin.readline().split())
visit_counts = list(map(int, stdin.readline().split()))

max_visit, count = sum(visit_counts[:x]), 1
current_visit = max_visit

for i in range(x, len(visit_counts)):
    current_visit = current_visit - visit_counts[i - x] + visit_counts[i]
    if current_visit > max_visit:
        max_visit, count = current_visit, 0
    elif current_visit < max_visit:
        continue
    count += 1
        
if max_visit == 0:
    print("SAD")
else:
    print(max_visit, count, sep='\n')