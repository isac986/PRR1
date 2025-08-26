telefonbok = {
    "isac" : "0763906200",
    "melker" : "0739921388",
    "mio" : "0765798135"
}

while True:

    val = int(input("\n1. Lägg till kontakt\n2. Sök bland kontakter\n3. updatera kontakt\n4. ta bort kontakt\n5. Avsluta:"))

    #Val 1 Lägger till person
    if val == 1:
        ny_namn = input("Namn: ")
        ny_nummer = input("Mobil nummer: ")
        
        telefonbok[ny_namn] = ny_nummer
        print(f"{ny_namn}, {ny_nummer} har lagts till.")

    #Val 2 Söker upp person
    elif val == 2:
        visa_person = input("Vems mobil nummer vill du se: ")
        
        if visa_person in telefonbok:
            print(f"{visa_person}: {telefonbok[visa_person]}")
        else:
            print (f"Det finns ingen {visa_person} i telefonboken")
        
    #Val 3 Redigerar person
    elif val == 3:
        uppdatera_person =input("Vem vill du göra ändringar på: ")
        
        if uppdatera_person in telefonbok:
            nytt_nummer = int(input("Ange nytt mobil nummer:"))
            print(f"{uppdatera_person}s nummer har uppdaterats till {nytt_nummer}.")
        else:
            print(f"Det finns ingen {uppdatera_person} i telfonboken.")
            
    #Val 4 Tar bort person
    elif val == 4:
        tabort_person = input("Vem vill du ta bort: ")
        
        if tabort_person in telefonbok:
            ja_nej = input(f"Är du säker att du vill ta bort {tabort_person} (j/n)")
            
            if ja_nej == "j":
                del telefonbok[tabort_person]
                print(f"{tabort_person} har blivit bort tagen")
            
            elif ja_nej == "n":
                print("Okej")
            
            else:
                print(f"Det finns ingen {tabort_person} i telefonboken")
    
    #Val 5 Avslutar            
    elif val == 5:
        break