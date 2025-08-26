def skottår (år):

 if (årtal%4 == 0 and årtal%100 != 0) or årtal%400 == 0 :
    return (True)
 else:
    return (False)

årtal = int(input ("Skriv årtalet"))
print (skottår(årtal))