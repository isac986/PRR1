def näst_största(lst):
    
    största = 0
    näst_största = 0
    
    
    for i in lista:
        if int(i) > int(största):
            näst_största = största
            största = i
    return näst_största


tal = input("Skriv några tal: ")
lista = tal.split()
     
print(näst_största(lista))