from sys import stdin

log, dic = int(stdin.readline()), {'enter':set()}
for i in range(log):
    name, work = stdin.readline().split()
    if work == 'leave' and name in dic['enter']:
        dic['enter'].remove(name)
    else: dic['enter'].add(name)

print('\n'.join(sorted(dic['enter'], reverse=True)))
