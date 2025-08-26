tal = input("Skriv några tal: ")
negativ = 0

lista = tal.split()

for i in lista:
    if float(i) < 0:
        negativ += 1 

print (negativ)
