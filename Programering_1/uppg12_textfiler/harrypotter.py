
file = open("C:/Users/isac.eriksson1/PRR1/python/Skola/uppg12/harryp.txt", "r")

innehåll = file.read()

tecken = len(innehåll)
rader = file.readlines()
längd = len(rader)
antal_ord = len(innehåll.split())
antal_meningar = innehåll.count(".") + innehåll.count("!") + innehåll.count("?")
harry = innehåll.count("harry") + innehåll.count("Harry")

file.seek(0)
rader = file.readlines()
längd = len(rader)

print(f"Rader: {längd}\nTecken: {tecken}\nOrd: {antal_ord}\nMeningar: {antal_meningar}\nHarry: {harry}")


file.close()