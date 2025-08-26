file = "fil_som_inte_finns"

try:
    with open(file, 'r') as fil:
        innehall = fil.read()
        print("Innehållet i filen:")
        print(innehall)

except FileNotFoundError:
    print(f"Filen finns inte.")
