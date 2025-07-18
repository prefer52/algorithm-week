from sys import stdin

n, m = map(int, stdin.readline().split())
true_info = stdin.readline().split()
true_count, true_people = 0, []
if len(true_info) == 1:
    true_count = 0
else:
    true_count = int(true_info[0])
    true_people = list(map(int, true_info[1:]))

group_infos = [[] for _ in range(n+1)]
person_infos = []
for i in range(m):
    person_list = list(map(int, stdin.readline().split()))[1:]
    person_infos.append(person_list)
    for person in person_list:
        group_infos[person].append(i)

true_groups = [False]*m
stack = []
stack.extend(true_people)
while stack:
    true_person = stack.pop()
    for group in group_infos[true_person]:
        if not true_groups[group]:
            true_groups[group] = True
            stack.extend(person_infos[group])
            
print(len(list(filter(lambda x: x is False, true_groups))))