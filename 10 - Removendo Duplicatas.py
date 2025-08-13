def duoremover (numbers):
    duos = 0
    newlist = []
    for i in numbers:
        if i not in newlist:
            newlist.append(i)
    return newlist

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

result = duoremover (numeros)
print (result)