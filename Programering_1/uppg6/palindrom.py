mening = input ("Skriv en text: ")
färdig_mening = mening.replace (" ","")

if färdig_mening == färdig_mening [::-1]:
    print ("Din mening är en palindrom")
    
else:
    print ("Din mening är inte en plindrom")