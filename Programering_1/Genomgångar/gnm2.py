# variabler, input, casting

namn = "isac" # string
ålder = 16 # int
adress = "tollare_kaj" # string
snusar = False # bool

#print (namn, ålder, adress, snusar)

text = f"Namn: {namn} \nÅlder: {ålder} \nAdress: {adress}"
print (text)

#input ("Tryck enter för att forsätta...")
annat_namn = input ("Vad heter du?") 
print (f"hej {annat_namn}! Trevligt att mötas")

# casting = ändra på en variabel typ och gör om den till en annan

annat_ålder = int (input (f"Hur gammal är du?, {annat_namn}?"))
#går att ändra till vilken variable typ som hälst på detta sätt