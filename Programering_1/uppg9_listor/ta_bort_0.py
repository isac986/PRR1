tal = input ("Skriv några tal: ")
lista = tal.split()

for i in lista:
    if int(i) == 0:
        lista.remove ("0")
        
print (lista)