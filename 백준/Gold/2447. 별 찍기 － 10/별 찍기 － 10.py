def fill_star(arr, n, r, c):
    if n == 3:
        arr[r-2][c-2] = ' '
    else:
        for i in range(3):
            fill_star(arr, n//3, r - (n//3)*2, c - (n//3)*i)
            fill_star(arr, n//3, r, c - (n//3)*i)
            
        fill_star(arr, n//3, r - (n//3), c - (n//3)*2)
        for i in range(r - (n//3)*2, r - (n//3)):
            for j in range(c - (n//3)*2, c - (n//3)):
                arr[i][j] = ' '
        fill_star(arr, n//3, r - (n//3), c)
                
n = int(input())
small_arr = ['*']*n
arr = []
for i in range(n):
    arr.append(small_arr[:])

fill_star(arr, n, n, n)
for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()