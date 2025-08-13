def ocurrences (list, number):
    count = 0
    for i in list:
        if number == i:
            count += 1
    return count 

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

value = int(input("Informe um valor para que o programa diga quantas vezes ele se repete na lista: "))
result = ocurrences(numeros, value)
print (result)