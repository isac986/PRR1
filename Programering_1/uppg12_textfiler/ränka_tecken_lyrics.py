file = open("C:/Users/isac.eriksson1/PRR1/python/Skola/uppg12/lyrics.txt", "r")

innehåll = file.read()

tecken = len(innehåll)

file.seek(0)

rader = file.readlines()
längd = len(rader)

print(f"Det finns {längd} rader och det finns {tecken} tecken")


file.close()