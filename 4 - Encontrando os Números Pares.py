def numpar (numer):
    pares = []
    for i in numer:
        if i % 2 == 0:
            pares.append(i)
    return pares 

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
listinha_massa = numpar(numeros)
print(listinha_massa)