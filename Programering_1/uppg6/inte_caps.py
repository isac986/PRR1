mening = input ("Skriv en mening: ")
if mening.isupper():
    print ("SLUTA SKRIKA!")

försök2 = input ("Gör ett nytt försök: ")


if försök2[0].isupper() and försök2[-1] in ".?!":
    print ("Bra jobbat ser bra ut!")
    
    
else:
    print ("Din meing är fett ful!!")