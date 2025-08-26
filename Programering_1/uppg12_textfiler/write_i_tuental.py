inehåll = ""

with open("C:/Users/isac.eriksson1/PRR1/python/Skola/uppg12/tusen_tal.txt", "r") as tusental:
    inehåll = tusental.read()
    
with open("C:/Users/isac.eriksson1/PRR1/python/Skola/uppg12/tusen_tal.txt", "w") as ny_file:
    ny_file.write ("Här börjar filen\n")
    ny_file.write(inehåll)
    ny_file.write ("\nhär slutar filen")
    