tal = input ("Skriv några tal: ")

lista1 = tal.split()

lista2 = []
lista3 = []

for i in lista1:
    if int(i) % 2:
        lista2.append(i)
    else:
        lista3.append(i)

print (lista2)
print (lista3)