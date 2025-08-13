def recievelist (list):
    if not list:
         return True
    else:
        return False

def createlist (): 
    newlist = []
    print("Escreva algo que queira que seja adicionado a lista, quando desejar parar de adicionar itens, basta digitar 'sair'")
    while True:
        item = input("Oque quer adicionar a lista? ")
        if item.lower() == "sair":
            break
        newlist.append(item)
    return newlist

newl = createlist()
result = recievelist(newl)
print (result)