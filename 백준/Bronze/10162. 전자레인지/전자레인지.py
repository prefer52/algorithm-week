time = int(input())
a_touch, time = time//300, time%300
b_touch, time = time//60, time%60
c_touch, time = time//10, time%10
print(-1 if time else f'{a_touch} {b_touch} {c_touch}')