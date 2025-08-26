tal1 = int(input("Skriv ett tal: "))
tal2 = int(input("Skriv ett till tal: "))
räknesätt = input("Välj räknesätt (+, -, *, /): ")

try:
    if räknesätt == "+":
        resultat = tal1 + tal2
    
    elif räknesätt == "-":
        resultat = tal1 - tal2

    elif räknesätt == "*":
        resultat = tal1 * tal2

    elif räknesätt == "/":
        if tal2 == 0:
            raise ZeroDivisionError("Kan inte dela med 0!")
        resultat = tal1 / tal2
    
    else:
        raise ValueError("Ogiltig operation! Välj mellan +, -, *, /.")

    print(f"Resultatet är: {resultat}")

except ValueError as ve:
    print(f"Fel: {ve}")
except ZeroDivisionError as zde:
    print(f"Fel: {zde}")
except Exception as e:
    print(f"Oförutsett fel: {e}")