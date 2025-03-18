S = input().strip()
print(" ".join([str(S.count(chr(ord('a') + i))) for i in range(26)]))