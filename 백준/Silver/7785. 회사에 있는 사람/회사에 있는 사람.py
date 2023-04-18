from sys import stdin

log = int(stdin.readline())
dic = {'enter':set()}
for i in range(log):
    name, work = stdin.readline().split()
    if work == 'leave' and name in dic['enter']:
        dic['enter'].remove(name)
    else: dic['enter'].add(name)

print('\n'.join(sorted(dic['enter'], reverse=True)))