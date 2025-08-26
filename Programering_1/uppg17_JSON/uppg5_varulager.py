import json

fil_väg = "C:/Users/isac.eriksson1/PRR1/python/Skola/uppg17_JSON/uppg5_artirklar.json"

with open(fil_väg, "r") as fil:
    varulager = json.load(fil)

def ny_artikel():
    artikelbeteckning = input("Ange artikelbeteckning (kod): ")
    artikelbeskrivning = input("Ange artikelbeskrivning: ")
    antal = input("Ange antal i lager: ")
    pris = input("Ange försäljningspris: ")

    varulager[artikelbeteckning] = {
        "beskrivning": artikelbeskrivning,
        "antal": antal,
        "pris": pris
    }

def spara_fil():
    with open(fil_väg, "w") as fil:
        json.dump(varulager, fil, indent=4)

while True:
    
    val = input("1. Lägg till artikel\n2. Visa lager\n3. Avsluta\nSvar: ")

    if val == "1":
        ny_artikel()
    elif val == "2":
        for key, value in varulager.items():
            print(f"{key}: {value}")
    elif val == "3":
        spara_fil()
        break