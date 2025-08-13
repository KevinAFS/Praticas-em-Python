def searnum (list, num):
        if num in list:
            return True 
        else: return False

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

sear = int(input("Digite um número para busca-lo na lista: "))
result = searnum (numeros, sear)
print (result)