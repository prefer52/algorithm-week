from sys import stdin
from itertools import combinations


n = int(stdin.readline())
power_list = [list(map(int, stdin.readline().split())) for _ in range(n)]

min_power_difference = 1e9
for link_team in tuple(combinations(range(n), n//2)):
    start_team = list(set(range(n)) - set(link_team))
    link_power_sum = sum(power_list[link_team[i]][link_team[j]] + power_list[link_team[j]][link_team[i]] for i in range(n//2) for j in range(i+1, n//2))
    start_power_sum = sum(power_list[start_team[i]][start_team[j]] + power_list[start_team[j]][start_team[i]] for i in range(n//2) for j in range(i+1, n//2))
    min_power_difference = min(min_power_difference, abs(link_power_sum - start_power_sum))
    
print(min_power_difference)