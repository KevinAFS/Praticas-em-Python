def secbig_num (numbers):
    big = float("-inf")
    sec = float("-inf")

    for i in numbers:
        if i > big:
            sec = big
            big = i

        elif i > sec and i != big:
            sec = i

    return sec

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

segundo = secbig_num(numeros)
print(segundo)