def solution(n, arr1, arr2):
    decrypt_arr1, decrypt_arr2 = [], []
    for crypt_code in arr1:
        decrypt_code = bin(crypt_code)[2:]
        decrypt_arr1.append('0'*(n-len(decrypt_code)) + decrypt_code)

    for crypt_code in arr2:
        decrypt_code = bin(crypt_code)[2:]
        decrypt_arr2.append('0'*(n-len(decrypt_code)) + decrypt_code)
    
    result = []
    for i in range(len(arr1)):
        overlap_str = bin(int(decrypt_arr1[i], 2) | int(decrypt_arr2[i], 2))[2:]
        result.append(str('0'*(n-len(overlap_str)) + overlap_str).replace('1', '#').replace('0', ' '))
        
    return result