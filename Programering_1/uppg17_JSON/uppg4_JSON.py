import json

fil_väg = "C:/Users/isac.eriksson1/PRR1/python/Skola/uppg17_JSON/uppg4.json"
    
with open(fil_väg, "r") as min_fil:
    andra_lista = json.load(min_fil)

for key, value in andra_lista.items():
    print(f"{key} : {value}")