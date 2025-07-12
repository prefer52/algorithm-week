from sys import stdin

n = int(stdin.readline())
l, m, r = map(int, stdin.readline().split())
min_l, min_m, min_r = l, m, r
for i in range(1, n):
    cur_l, cur_m, cur_r = map(int, stdin.readline().split())
    l, m, r = cur_l + max(l, m), cur_m + max(l, m, r), cur_r + max(m, r)
    min_l, min_m, min_r = cur_l + min(min_l, min_m), cur_m + min(min_l, min_m, min_r), cur_r + min(min_m, min_r)

print(max(l, m, r), min(min_l, min_m, min_r))