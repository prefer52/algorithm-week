n = int(input())
in_attack_col = [False]*n
in_attack_rd_diag, in_attack_ld_diag = [False]*(2*n - 1), [False]*(2*n - 1)
result = 0

def backtracking(cur_row, col_sets):
    if cur_row == n:
        global result
        result += 1
        return
    
    for j in list(col_sets):
        if not any([in_attack_rd_diag[j + (n - 1 - cur_row)], in_attack_ld_diag[j + cur_row]]):
            in_attack_rd_diag[j + (n - 1 - cur_row)], in_attack_ld_diag[j + cur_row] = True, True
            col_sets.remove(j)
            backtracking(cur_row+1, col_sets)
            in_attack_rd_diag[j + (n - 1 - cur_row)], in_attack_ld_diag[j + cur_row] = False, False
            col_sets.add(j)


backtracking(0, set(i for i in range(n)))
print(result)