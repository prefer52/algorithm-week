from sys import stdin

n, m = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))
for i in range(1, n):
    numbers[i] += numbers[i-1]

mods = [numbers[i]%m for i in range(n)]
mod_m_count = [0]*(m+1)
for index in range(n):
    mod_m_count[mods[index]] += 1

print(mod_m_count[0]*(mod_m_count[0]+1)//2 + sum(mod_m_count[i]*(mod_m_count[i]-1)//2 for i in range(1, m)))