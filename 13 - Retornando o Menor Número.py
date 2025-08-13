def snencounter (numbers):
    so = numbers[0]
    for i in numbers:
        if i < so:
            so = i
    return so

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

smallest = snencounter(numeros)
print (smallest)