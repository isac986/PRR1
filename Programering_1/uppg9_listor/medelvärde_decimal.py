tal = input("Skriv några decimaltal: ")

lista = tal.split()

tot = 0

for i in lista:
    tot += float(i)


medelvärde = tot/len(lista)

print (medelvärde)