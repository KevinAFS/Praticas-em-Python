def biggest_num (numbers):
    big = numbers[0]
    for i in numbers:
        if i > big:
            big = i
    return big

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

maior = biggest_num (numeros)
print (maior)
