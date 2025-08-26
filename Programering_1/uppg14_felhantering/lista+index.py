def lista_tal(list, index):
    try:
        return list[index]
    except IndexError:
        return f"fel: index {index} är inte med i listan"
    
lista = [5, 4, 3 ,2 ,1]

print(lista_tal(lista, 2))

print(lista_tal(lista, 5))